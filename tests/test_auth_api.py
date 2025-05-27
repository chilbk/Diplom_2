import pytest
import allure
from Diplom_2.apicontroller.auth_api import UserProfileApi
from Diplom_2.auth_helper import AuthHelper
from Diplom_2.data import UNAUTHORIZED_MESSAGE

helper = AuthHelper()


@allure.suite("Тесты на изменение данных пользователя")
class TestAuthApi:

    @pytest.mark.parametrize("field, value", [
        ("name", "UpdatedName"),
        ("email", "updatedemail@example.com")
    ])
    @allure.title("Обновление поля пользователя с авторизацией: {field}")
    def test_update_user_with_auth(self, user_token, field, value):
        api = UserProfileApi()

        # Генерация уникального email, если тестирует поле email
        if field == "email":
            value = AuthHelper().generate_login()

        new_data = {field: value}

        with allure.step(f"Отправка запроса PATCH с токеном и полем {field}"):
            response = api.update_user_with_auth(user_token, new_data)

        with allure.step("Проверка успешного обновления данных"):
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