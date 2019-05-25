from enum import Enum


class CityEnum(Enum):
    """
           This enumerator is used for the User registration model.
           It contains all the possible choices for the city field MyUser
           charfield.
           It inherits the the Enum model from the enum application.

           """
    SA = 'Sofia'
    PB = 'Plovdiv'
    PA = 'Pazardjik'
    A = 'Burgas'
    B = 'Varna'


class TitleEnum(Enum):
    """
              This enumerator is used for the User registration model.
              It contains all the possible choices for the personal title field
              in MyUser charfield.
              It inherits the the Enum model from the enum application.

              """
    Mr = 'Mr'
    Mrs = 'Mrs'
    Ms = 'Ms'


class DoctorTitle(Enum):
    """
                 This enumerator is used for the User registration model.
                 It contains all the possible choices for the doctor title field
                 in Veterinary doctor charfield.
                 It inherits the the Enum model from the enum application.

                 """

    Dr = 'Doctor'
    Prof = 'Professor'
