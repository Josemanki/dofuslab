/** @jsxImportSource @emotion/react */

import * as React from 'react';

import { Card, Skeleton } from 'antd';
import { useQuery } from '@apollo/client';
import { useTheme } from '@emotion/react';

import { classes } from 'graphql/queries/__generated__/classes';
import classesQuery from 'graphql/queries/classes.graphql';
import {
  classById,
  classByIdVariables,
} from 'graphql/queries/__generated__/classById';
import classByIdQuery from 'graphql/queries/classById.graphql';
import { itemCardStyle } from 'common/mixins';
import { CustomSetContext } from 'common/utils';
import SpellVariantPairCard from './SpellVariantPairCard';

interface Props {
  dofusClassId?: string;
}

const ClassicClassSpells: React.FC<Props> = ({ dofusClassId }) => {
  const { customSet } = React.useContext(CustomSetContext);
  const { data } = useQuery<classes>(classesQuery);
  const theme = useTheme();

  const { data: classData, loading: classDataLoading } = useQuery<
    classById,
    classByIdVariables
  >(classByIdQuery, {
    variables: { id: dofusClassId },
    skip: !dofusClassId,
  });

  const spellVariantPairs = classData?.classById?.spellVariantPairs;

  if (!data) {
    return null;
  }

  if (classDataLoading) {
    return (
      <>
        {Array(22)
          .fill(null)
          .map((_, idx) => (
            <Card
              size="small"
              // eslint-disable-next-line react/no-array-index-key
              key={idx}
              css={{
                ...itemCardStyle,
                border: `1px solid ${theme.border?.default}`,
                background: theme.layer?.background,
              }}
            >
              <Skeleton loading title active paragraph={{ rows: 6 }} />
            </Card>
          ))}
      </>
    );
  }

  if (!spellVariantPairs) {
    return null;
  }

  return (
    <>
      {spellVariantPairs.map((pair) => (
        <SpellVariantPairCard
          key={pair.id}
          spellVariantPair={pair}
          customSet={customSet}
        />
      ))}
    </>
  );
};

export default ClassicClassSpells;
