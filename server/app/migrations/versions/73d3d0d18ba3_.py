"""empty message

Revision ID: 73d3d0d18ba3
Revises: 8b23da1cb2e1
Create Date: 2020-12-29 20:01:07.345366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "73d3d0d18ba3"
down_revision = "8b23da1cb2e1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "buff",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        type_=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "equipped_item_exo",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        type_=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "item_stat",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        type_=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "set_bonus",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        type_=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "set_bonus",
        "stat",
        existing_type=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        type_=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "item_stat",
        "stat",
        existing_type=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        type_=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "equipped_item_exo",
        "stat",
        existing_type=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        type_=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "buff",
        "stat",
        existing_type=sa.Enum(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            "CRITICAL_FAILURE",
            "NEUTRAL_RES_PVP",
            "PCT_NEUTRAL_RES_PVP",
            "EARTH_RES_PVP",
            "PCT_EARTH_RES_PVP",
            "FIRE_RES_PVP",
            "PCT_FIRE_RES_PVP",
            "WATER_RES_PVP",
            "PCT_WATER_RES_PVP",
            "AIR_RES_PVP",
            "PCT_AIR_RES_PVP",
            "HP",
            name="stat",
        ),
        type_=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
