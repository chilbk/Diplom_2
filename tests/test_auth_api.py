import pytest
import allure
from Diplom_2.apicontroller.auth_api import UserProfileApi
from Diplom_2.auth_helper import AuthHelper
from Diplom_2.data import UNAUTHORIZED_MESSAGE

@allure.suite("Тесты на изменение данных пользователя")
class TestAuthApi:
    @allure.title("Обновление имени пользователя с авторизацией")
    def test_update_user_name_with_auth(self, user_token):
        api = UserProfileApi()
        new_data = {"name": "UpdatedName"}

        with allure.step("Отправка PATCH запроса с токеном и новым именем"):
            response = api.update_user_with_auth(user_token, new_data)

        with allure.step("Проверка успешного обновления имени"):
            assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"

    @allure.title("Обновление email пользователя с авторизацией")
    def test_update_user_email_with_auth(self, user_token):
        api = UserProfileApi()
        new_email = AuthHelper().generate_login()
        new_data = {"email": new_email}

        with allure.step("Отправка PATCH запроса с токеном и новым email"):
            response = api.update_user_with_auth(user_token, new_data)

        with allure.step("Проверка успешного обновления email"):
            assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"

    @pytest.mark.parametrize("field, value", [
        ("name", "NoAuthName"),
        ("email", "noauth@example.com")
    ])
    @allure.title("Обновление поля пользователя без авторизации: {field}")
    def test_update_user_without_auth(self, field, value):
        api = UserProfileApi()
        new_data = {field: value}

        with allure.step("Отправка запроса PATCH без токена"):
            response = api.update_user_without_auth(new_data)

        with allure.step("Проверка ошибки авторизации"):
            assert response.status_code == 401, f"Ожидали 401, получили {response.status_code}. Ответ: {response.text}"
            assert response.json()["message"] == UNAUTHORIZED_MESSAGE, "Некорректное сообщение об ошибке"