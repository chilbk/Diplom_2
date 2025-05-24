import pytest
import allure
from Diplom_2.apicontroller.auth_api import UserProfileApi
from Diplom_2.auth_helper import AuthHelper

helper = AuthHelper()

@pytest.mark.parametrize("field, value", [
    ("name", "UpdatedName"),
    ("email", helper.generate_login())
])
@allure.title("Обновление поля пользователя с авторизацией: {field}")
def test_update_user_with_auth(user_token, field, value):
    api = UserProfileApi()
    new_data = {field: value}

    with allure.step(f"Отправка запроса PATCH с токеном и полем {field}"):
        response = api.update_user_with_auth(user_token, new_data)

    with allure.step("Проверка успешного обновления данных"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"
        body = response.json()
        assert body['success'] is True, f"Ожидали success=True. Ответ: {body}"
        assert body['user'][field] == value, f"Поле {field} не обновлено: {body}"


@pytest.mark.parametrize("field, value", [
    ("name", "HackerName"),
    ("email", "hacker@example.com")
])
@allure.title("Попытка обновления поля без авторизации: {field}")
def test_update_user_without_auth(field, value):
    api = UserProfileApi()
    new_data = {field: value}

    with allure.step(f"Отправка запроса PATCH без токена с полем {field}"):
        response = api.update_user_without_auth(new_data)

    with allure.step("Проверка отказа в доступе"):
        assert response.status_code == 401, f"Ожидали 401, получили {response.status_code}. Ответ: {response.text}"
        body = response.json()
        assert body['message'] == "You should be authorised", f"Неверное сообщение об ошибке: {body}"