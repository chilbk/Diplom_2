import pytest
from apicontroller.reg_api import UserApi
from apicontroller.login_api import LoginApi

@pytest.fixture
def user_data():
# Эта фикстура создаёт уникального пользователя
    api = UserApi()
    response, data = api.create_unique_user()
    return data  # возвращаем email, password, name

@pytest.fixture
def user_token(user_data):
# Эта фикстура авторизует пользователя и возвращает токен для запросов с аторизацией
    email = user_data['email']
    password = user_data['password']
    api = LoginApi()
    response = api.login_with_valid_credentials(email, password)
    token = response.json().get('accessToken')
    return token