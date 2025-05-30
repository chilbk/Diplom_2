existing_user = {
    "email": "pythonvda@mail.ru",
    "password": "qwerty123",
    "name": "Dmitry"
}

UNAUTHORIZED_MESSAGE = "You should be authorised"
USER_EXISTS_MESSAGE = "User already exists"
INVALID_CREDENTIALS_MESSAGE = "email or password are incorrect"
MISSING_FIELDS_MESSAGE = "Email, password and name are required fields"

INVALID_LOGIN_CREDENTIALS = [
    ("invalid@example.com", "wrongpass"),
    ("", "validpass"),
    ("valid@example.com", ""),
    ("", "")
]