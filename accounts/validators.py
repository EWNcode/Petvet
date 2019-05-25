from django.core import validators


class PhoneValidator(validators.RegexValidator):
    """
                      This validator is used to make sure that upon user
                      registration, his/her phone number will be saved in the data base
                      starting with 0 and have 9 additional following digits.

                      """
    regex = r'(^0\w{9}$)'
    message = ("Phone number must be entered in the format: '0123456789'. Up to 10 digits allowed.")
    flags = 0