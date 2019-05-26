from django.core import validators


class NameValidator(validators.RegexValidator):
    """
                      This validator is used to make sure that upon user
                      registration all his/her name will be saved in the data base
                      is starting with a capital letter and is followed by at least one lower case letter.

                      """
    regex = r'(^[A-Z][a-z]+$)'
    message = ("Name must contain only letters and should start with a capital Letter. example:'Barri'")
    flags = 0