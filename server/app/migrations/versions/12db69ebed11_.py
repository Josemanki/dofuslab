"""empty message

Revision ID: 12db69ebed11
Revises: 47c0338ee9ff
Create Date: 2020-04-21 23:15:59.424460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from app.database.model_item_slot import ModelItemSlot
from app.database.model_item_slot_translation import ModelItemSlotTranslation
from app.database.model_item_type import ModelItemType
from app.database.model_item_type_translation import ModelItemTypeTranslation
import os
import json
from sqlalchemy.orm.session import Session

dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# revision identifiers, used by Alembic.
revision = "12db69ebed11"
down_revision = "bc6df2e88154"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item_type_translation",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("item_type_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("locale", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_type_id"],
            ["item_type.uuid"],
            name=op.f("fk_item_type_translation_item_type_id_item_type"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_item_type_translation")),
        sa.UniqueConstraint("id", name=op.f("uq_item_type_translation_id")),
    )

    session = Session(bind=op.get_bind())

    with open(os.path.join(dirname, "database/data/item_types.json"), "r") as file:
        data = json.load(file)
        conn = op.get_bind()

        for record in data:
            res = conn.execute(
                "select * from item_type where item_type.name = '{}'".format(
                    record["en"]
                )
            )
            results = res.fetchall()

            for locale in record:
                if len(results) == 0:
                    break
                translation = ModelItemTypeTranslation(
                    item_type_id=results[0][0], locale=locale, name=record[locale]
                )
                session.add(translation)

        session.commit()

    op.create_table(
        "item_slot_translation",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("item_slot_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("locale", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_slot_id"],
            ["item_slot.uuid"],
            name=op.f("fk_item_slot_translation_item_slot_id_item_slot"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_item_slot_translation")),
        sa.UniqueConstraint("id", name=op.f("uq_item_slot_translation_id")),
    )

    with open(os.path.join(dirname, "database/data/item_slots.json"), "r") as file:
        data = json.load(file)
        i = 0
        for record in data:
            for _ in range(record.get("quantity", 1)):
                conn = op.get_bind()
                res = conn.execute(
                    "select * from item_slot where item_slot.name = '{}' and item_slot.order = '{}'".format(
                        record["name"]["en"], i
                    )
                )
                results = res.fetchall()

                for locale in record["name"]:
                    if len(results) == 0:
                        break
                    translation = ModelItemSlotTranslation(
                        item_slot_id=results[0][0],
                        locale=locale,
                        name=record["name"][locale],
                    )
                    session.add(translation)
                i = i + 1
        session.commit()

    op.drop_column("item_slot", "name")
    op.drop_column("item_type", "name")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "item_type",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
    )

    session = Session(bind=op.get_bind())
    conn = op.get_bind()

    all_types = session.query(ModelItemType).all()
    for type in all_types:
        en_translation = (
            session.query(ModelItemTypeTranslation)
            .filter_by(locale="en", item_type_id=type.uuid)
            .one()
        )
        conn.execute(
            "UPDATE item_type SET name='{}' WHERE uuid='{}'".format(
                en_translation.name, en_translation.item_type_id
            )
        )

    op.alter_column("item_type", "name", nullable=False)

    op.add_column(
        "item_slot",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
    )

    all_slots = session.query(ModelItemSlot).all()
    for slot in all_slots:
        en_translation = (
            session.query(ModelItemSlotTranslation)
            .filter_by(locale="en", item_slot_id=slot.uuid)
            .one()
        )
        conn.execute(
            "UPDATE item_slot SET name='{}' WHERE uuid='{}'".format(
                en_translation.name, en_translation.item_slot_id
            )
        )

    op.alter_column("item_slot", "name", nullable=False)

    op.drop_table("item_type_translation")
    op.drop_table("item_slot_translation")
    # ### end Alembic commands ###
