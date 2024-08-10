import secrets
import string


def generate_password(user_data):
    password_settings = user_data["password_settings"]
    min_length = password_settings["length"]["min_length"]
    max_length = password_settings["length"]["max_length"]
    total_length = password_settings["length"]["total_length"]
    fixed_length = password_settings["length"]["fixed_length"]

    include_uppercase = password_settings["include_uppercase"]
    include_lowercase = password_settings["include_lowercase"]
    include_digits = password_settings["include_digits"]
    include_specials = password_settings["include_specials"]

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character sets selected for password generation")

    if fixed_length:
        length = total_length
    else:
        length = secrets.choice(range(min_length, max_length + 1))

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password
