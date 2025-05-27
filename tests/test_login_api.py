import pytest
import allure
from Diplom_2.apicontroller.login_api import LoginApi
from Diplom_2.data import INVALID_CREDENTIALS_MESSAGE

@allure.suite("Тесты на авторизацию")
class TestLoginApi:

    @allure.title("Успешная авторизация с корректными данными")
    def test_login_with_valid_credentials(self, user_data):
        api = LoginApi()

        with allure.step("Отправка запроса авторизации с валидными данными"):
            response = api.login_with_valid_credentials(user_data['email'], user_data['password'])

        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"
            body = response.json()
            assert body['success'] is True, f"Ожидали success=True. Ответ: {body}"
            assert 'accessToken' in body, "accessToken отсутствует в ответе"
            assert body['user']['email'] == user_data['email'], f"Email не совпадает: {body}"

    @pytest.mark.parametrize("email, password", [
        ("invalid@example.com", "wrongpass"),
        ("", "validpass"),
        ("valid@example.com", ""),
        ("", "")
    ])
    @allure.title("Попытка авторизации с невалидными данными: email={email}, password={password}")
    def test_login_with_invalid_credentials(self, email, password):
        api = LoginApi()

        with allure.step("Отправка запроса авторизации с невалидными данными"):
            response = api.login_with_invalid_credentials(email, password)

        with allure.step("Проверка ошибки авторизации"):
            assert response.status_code == 401, f"Ожидали 401, получили {response.status_code}. Ответ: {response.text}"
            body = response.json()
            assert body['message'] == INVALID_CREDENTIALS_MESSAGE, f"Неверное сообщение: {body}"