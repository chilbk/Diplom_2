import requests
from Diplom_2.api_endpoints import LOGIN_ENDPOINT

class LoginApi:
# Метод login_with_valid_credentials выполняет логин с корректными данными
    def login_with_valid_credentials(self, email, password):

        payload = {
            'email': email,
            'password': password
        }
        response = requests.post(LOGIN_ENDPOINT, json=payload)
        return response
# Метод login_with_invalid_credentials выполняет логин с некорректными данными
    def login_with_invalid_credentials(self, email, password):
        payload = {
            'email': email,
            'password': password
        }
        response = requests.post(LOGIN_ENDPOINT, json=payload)
        return response
