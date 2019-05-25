from enum import Enum


class AnimalKind(Enum):
    """
               This enumerator is used for the Animal registration model.
               It contains all the possible choices for the animal type field.
               It inherits the the Enum model from the enum application.

               """
    D = 'Dog'
    C = 'Cat'


class Gender(Enum):
    """
                  This enumerator is used for the Animal registration model.
                  It contains all the possible choices for the gender type field.
                  It inherits the the Enum model from the enum application.

                  """
    F = 'Female'
    M = 'Male'