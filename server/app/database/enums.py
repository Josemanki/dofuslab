from app import db
from enum import auto, Enum
import sqlalchemy


class BuildGender(Enum):
    MALE = auto()
    FEMALE = auto()


class Stat(Enum):
    VITALITY = auto()
    AP = auto()
    MP = auto()
    INITIATIVE = auto()
    PROSPECTING = auto()
    RANGE = auto()
    SUMMON = auto()
    WISDOM = auto()
    STRENGTH = auto()
    INTELLIGENCE = auto()
    CHANCE = auto()
    AGILITY = auto()
    AP_PARRY = auto()
    AP_REDUCTION = auto()
    MP_PARRY = auto()
    MP_REDUCTION = auto()
    CRITICAL = auto()
    HEALS = auto()
    LOCK = auto()
    DODGE = auto()
    PCT_FINAL_DAMAGE = auto()
    POWER = auto()
    DAMAGE = auto()
    CRITICAL_DAMAGE = auto()
    NEUTRAL_DAMAGE = auto()
    EARTH_DAMAGE = auto()
    FIRE_DAMAGE = auto()
    WATER_DAMAGE = auto()
    AIR_DAMAGE = auto()
    REFLECT = auto()
    TRAP_DAMAGE = auto()
    TRAP_POWER = auto()
    PUSHBACK_DAMAGE = auto()
    PCT_SPELL_DAMAGE = auto()
    PCT_WEAPON_DAMAGE = auto()
    PCT_RANGED_DAMAGE = auto()
    PCT_MELEE_DAMAGE = auto()
    NEUTRAL_RES = auto()
    PCT_NEUTRAL_RES = auto()
    EARTH_RES = auto()
    PCT_EARTH_RES = auto()
    FIRE_RES = auto()
    PCT_FIRE_RES = auto()
    WATER_RES = auto()
    PCT_WATER_RES = auto()
    AIR_RES = auto()
    PCT_AIR_RES = auto()
    CRITICAL_RES = auto()
    PUSHBACK_RES = auto()
    PCT_RANGED_RES = auto()
    PCT_MELEE_RES = auto()
    PODS = auto()


class WeaponEffectType(Enum):
    NEUTRAL_DAMAGE = auto()
    EARTH_DAMAGE = auto()
    FIRE_DAMAGE = auto()
    WATER_DAMAGE = auto()
    AIR_DAMAGE = auto()
    NEUTRAL_STEAL = auto()
    EARTH_STEAL = auto()
    FIRE_STEAL = auto()
    WATER_STEAL = auto()
    AIR_STEAL = auto()
    AP = auto()
    MP = auto()
    HP_RESTORED = auto()


class SpellEffectType(Enum):
    NEUTRAL_DAMAGE = auto()
    EARTH_DAMAGE = auto()
    FIRE_DAMAGE = auto()
    WATER_DAMAGE = auto()
    AIR_DAMAGE = auto()
    NEUTRAL_STEAL = auto()
    EARTH_STEAL = auto()
    FIRE_STEAL = auto()
    WATER_STEAL = auto()
    AIR_STEAL = auto()
    AP = auto()
    MP = auto()
    HP_RESTORED = auto()
    SHIELD = auto()
    PUSHBACK_DAMAGE = auto()
    BEST_ELEMENT_DAMAGE = auto()
    BEST_ELEMENT_STEAL = auto()


class WeaponElementMage(Enum):
    EARTH_85 = auto()
    EARTH_68 = auto()
    EARTH_50 = auto()
    FIRE_85 = auto()
    FIRE_68 = auto()
    FIRE_50 = auto()
    WATER_85 = auto()
    WATER_68 = auto()
    WATER_50 = auto()
    AIR_85 = auto()
    AIR_68 = auto()
    AIR_50 = auto()


BuildGenderEnum = sqlalchemy.Enum(BuildGender)
StatEnum = sqlalchemy.Enum(Stat)
WeaponEffectEnum = sqlalchemy.Enum(WeaponEffectType)
SpellEffectEnum = sqlalchemy.Enum(SpellEffectType)
WeaponElementMageEnum = sqlalchemy.Enum(WeaponElementMage)
