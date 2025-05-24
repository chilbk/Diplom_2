import requests
from Diplom_2.auth_helper import AuthHelper
from Diplom_2.api_endpoints import REGISTER_ENDPOINT


class UserApi:

# __init__ - конструктор
    def __init__(self):
        self.auth = AuthHelper()
# Метод create_unique_user - создает уникального пользователя
    def create_unique_user(self):
        email = self.auth.generate_login()
        password = self.auth.generate_password()
        name = self.auth.generate_name()

        payload = {
            'email': email,
            'password': password,
            'name': name
        }

        response = requests.post(REGISTER_ENDPOINT, json=payload)
        return response, payload

# Метод create_existing_user - пытается создать пользователя с уже существующими данными
    def create_existing_user(self):
        payload = {
            "email": "pythonvda@mail.ru",
            "password": "qwerty123",
            "name": "Dmitry"
        }

        response = requests.post(REGISTER_ENDPOINT, json=payload)
        return response

# Метод create_user_with_missing_fields - пытается создать пользователя без одного из обязательных полей
    def create_user_with_missing_fields(self):
        email = self.auth.generate_login()
        password = self.auth.generate_password()
        name = self.auth.generate_name()

        test_cases = [
            {"password": password, "name": name},              # Пользователь без email
            {"email": email, "name": name},                    # Пользователь без password
            {"email": email, "password": password}            # Пользователь без name
        ]

        responses = []
        for case in test_cases:
            response = requests.post(REGISTER_ENDPOINT, json=case)
            responses.append((case, response))

        return responses