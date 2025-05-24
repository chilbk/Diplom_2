import pytest
from Diplom_2.apicontroller.reg_api import UserApi
from Diplom_2.apicontroller.login_api import LoginApi

@pytest.fixture(scope='function')
def user_data():
# Эта фикстура создаёт уникального пользователя
    api = UserApi()
    response, data = api.create_unique_user()
    assert response.status_code == 200, 'Не удалось создать пользователя'
    return data

@pytest.fixture(scope='function')
def user_token(user_data):
# Эта фикстура авторизует пользователя и возвращает токен для запросов с аторизацией
    api = LoginApi()
    response = api.login_with_valid_credentials(user_data['email'], user_data['password'])
    assert response.status_code == 200, 'Не удалось авторизовать пользователя'
    token = response.json()['accessToken']
    return token