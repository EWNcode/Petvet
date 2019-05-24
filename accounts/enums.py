from enum import Enum


class CityEnum(Enum):
    SA = 'Sofia'
    PB = 'Plovdiv'
    PA = 'Pazardjik'
    A = 'Burgas'
    B = 'Varna'


class TitleEnum(Enum):
    Mr = 'Mr'
    Mrs = 'Mrs'
    Ms = 'Ms'


class DoctorTitle(Enum):
    Dr = 'DOCTOR'
    Prof = 'Professor'