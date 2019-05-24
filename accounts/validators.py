from django.core import validators


class PhoneValidator(validators.RegexValidator):
    regex = r'(^0\w{9}$)'
    message = ("Phone number must be entered in the format: '0123456789'. Up to 10 digits allowed.")
    flags = 0