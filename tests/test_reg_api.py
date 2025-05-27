import pytest
import allure
from Diplom_2.apicontroller.reg_api import UserApi


@allure.suite("Тесты регистрации пользователей")
class TestRegApi:

    @allure.title('Регистрация нового уникального пользователя')
    def test_register_unique_user(self):
        api = UserApi()

        with allure.step('Создание уникального пользователя'):
            response, payload = api.create_unique_user()

        with allure.step('Проверка успешной регистрации'):
            assert response.status_code == 200, f'Ожидали 200, получили {response.status_code}. Ответ: {response.text}'
            body = response.json()
            assert body['success'] is True, f'Ожидали success=True. Ответ: {body}'
            assert 'accessToken' in body, f'accessToken отсутствует в ответе: {body}'
            assert body['user']['email'] == payload['email'], f'Email в ответе не совпадает с отправленным: {body}'

    @allure.title('Попытка зарегистрировать уже существующего пользователя')
    def test_register_existing_user(self):
        api = UserApi()

        with allure.step('Попытка регистрации с уже существующими данными'):
            response = api.create_existing_user()

        with allure.step('Проверка сообщения об ошибке'):
            assert response.status_code == 403, f'Ожидали 403, получили {response.status_code}. Ответ: {response.text}'
            body = response.json()
            assert body['message'] == 'User already exists', f'Неверное сообщение: {body}'

    @pytest.mark.parametrize('case_index, field_name', [
        (0, 'email'),
        (1, 'password'),
        (2, 'name')
    ])
    @allure.title('Попытка регистрации без обязательного поля: {field_name}')
    def test_register_missing_fields(self, case_index, field_name):
        api = UserApi()

        with allure.step('Формирование и отправка запроса без одного из обязательных полей'):
            responses = api.create_user_with_missing_fields()
            data, response = responses[case_index]

        with allure.step('Проверка сообщения об ошибке'):
            assert response.status_code == 403, f'Ожидали 403, получили {response.status_code}. Ответ: {response.text}'
            body = response.json()
            assert body['message'] == 'Email, password and name are required fields', \
                f'Неверное сообщение об ошибке: {body}'
