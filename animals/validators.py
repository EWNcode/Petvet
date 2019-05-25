from django.core import validators


class SerialNumberValidator(validators.RegexValidator):
    """
                      This validator is used to make sure that the
                      the serial number input has exactly 10 symbols
                      of length. It can contain both digits and letters.

                      """
    regex = r'(^[a-zA-Z0-9]{10}$)'
    message = ("Animal serial number must contain exactly 10 symbols.")
    flags = 0