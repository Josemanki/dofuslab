/** @jsx jsx */

import React, { useEffect, useState } from 'react';
import { jsx } from '@emotion/core';
import { Modal, notification } from 'antd';
import { useRouter } from 'next/router';

import { useTranslation } from 'i18n';
import { getImageUrl } from 'common/utils';
import { PROFILE_PICTURES, mq } from '../../common/constants';
import { gray7, blue6 } from 'common/mixins';
import changeProfilePictureMutation from 'graphql/mutations/changeProfilePicture.graphql';
import {
  changeProfilePicture,
  changeProfilePictureVariables,
} from 'graphql/mutations/__generated__/changeProfilePicture';
import { useMutation } from '@apollo/client';
import userProfileQuery from 'graphql/queries/userProfile.graphql';
import buildListQuery from 'graphql/queries/buildList.graphql';

interface Props {
  username: string;
  visible: boolean;
  onCancel: () => void;
  currentlyActive: string;
}

const ProfilePictureModal: React.FC<Props> = ({
  username,
  onCancel,
  visible,
  currentlyActive,
}) => {
  const { t } = useTranslation('common');
  const [active, setActive] = useState<any>('');

  useEffect(() => {
    setActive(currentlyActive);
  }, []);
  const [profilePictureMutate, { loading: changePictureLoading }] = useMutation<
    changeProfilePicture,
    changeProfilePictureVariables
  >(changeProfilePictureMutation, {
    variables: { picture: active },
    refetchQueries: () => [
      {
        query: userProfileQuery,
        variables: {
          username: username,
        },
      },
      {
        query: buildListQuery,
        variables: {
          username,
          first: 20,
          filters: { search: '', tagIds: [] },
        },
      },
    ],
    awaitRefetchQueries: true,
  });
  const router = useRouter();

  const onChangePicture = React.useCallback(
    async (e: React.MouseEvent<HTMLElement>) => {
      e.stopPropagation();
      const { data } = await profilePictureMutate();
      onCancel();
      if (data?.changeProfilePicture?.ok) {
        notification.success({
          message: t('SUCCESS'),
          // Missing translation
          description: t('Profile picture changed successfully'),
        });
      }
    },
    [profilePictureMutate, router, onCancel],
  );

  const onCancelClick = React.useCallback(
    (e: React.MouseEvent<HTMLElement>) => {
      e.stopPropagation();
      setActive(currentlyActive);
      onCancel();
    },
    [onCancel],
  );

  return (
    <Modal
      visible={visible}
      // Missing translation
      title={'Change profile picture'}
      centered
      onOk={onChangePicture}
      onCancel={onCancelClick}
      confirmLoading={changePictureLoading}
      okText={t('OK')}
    >
      <div
        css={{ display: 'flex', justifyContent: 'center', marginBottom: 24 }}
      >
        <img
          src={getImageUrl(active)}
          // Missing translation
          alt="Currently selected profile picture"
          css={{ maxWidth: 220, borderRadius: 4 }}
        />
      </div>
      <div
        css={{
          display: 'flex',
          flexWrap: 'wrap',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '15px',
          maxHeight: '30vh',
          overflow: 'auto',
          [mq[1]]: {
            maxHeight: 'auto',
          },
        }}
      >
        {PROFILE_PICTURES.map((item, index) => {
          const activeStyle =
            active === item
              ? {
                  borderRadius: 4,
                  border: `2px solid ${blue6}`,
                  '&:hover': {
                    cursor: 'pointer',
                  },
                }
              : {
                  borderRadius: 4,
                  border: `1px solid ${gray7}`,
                  '&:hover': {
                    cursor: 'pointer',
                  },
                };

          return (
            <img
              src={getImageUrl(item)}
              key={`profile-pic-${index}`}
              // Missing translation
              alt="Profile picture"
              width={'100px'}
              onClick={() => {
                setActive(item);
              }}
              css={activeStyle}
            />
          );
        })}
      </div>
    </Modal>
  );
};

export default ProfilePictureModal;
