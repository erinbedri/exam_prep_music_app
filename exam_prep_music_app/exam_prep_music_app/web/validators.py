import re

from django.core.exceptions import ValidationError

USERNAME_CHAR_EXCEPTION = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_username_chars(username):
    if not re.match("^[A-Za-z0-9_]*$", username):
        raise ValidationError(USERNAME_CHAR_EXCEPTION)

