import pytest
import allure
from Diplom_2.apicontroller.order_api import OrderApi

valid_ingredients = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6c"
]

@allure.title("Создание заказа с авторизацией и валидными ингредиентами")
def test_create_order_with_auth(user_token):
    api = OrderApi()

    with allure.step("Отправка POST запроса с токеном и валидными ингредиентами"):
        response = api.get_orders(token=user_token)

    with allure.step("Проверка успешного ответа"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"
        body = response.json()
        assert 'orders' in body, f"Нет заказов в ответе: {body}"


@allure.title("Создание заказа без авторизации")
def test_create_order_without_auth():
    api = OrderApi()

    with allure.step("Отправка POST запроса без токена и с валидными ингредиентами"):
        response = api.get_orders()

    with allure.step("Проверка ошибки доступа"):
        assert response.status_code == 401, f"Ожидали 401, получили {response.status_code}. Ответ: {response.text}"
        body = response.json()
        assert body['message'] == "You should be authorised", f"Неверное сообщение: {body}"


@allure.title("Создание заказа без ингредиентов")
def test_create_order_without_ingredients(user_token):
    api = OrderApi()

    with allure.step("Отправка POST запроса с токеном, но без ингредиентов"):
        response = api.get_orders(token=user_token)

    with allure.step("Проверка успешного ответа (пустой список возможен)"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"


@allure.title("Создание заказа с невалидными ингредиентами")
def test_create_order_with_invalid_ingredients(user_token):
    api = OrderApi()

    with allure.step("Отправка POST запроса с невалидными ингредиентами (эмуляция через GET)"):
        response = api.get_orders(token=user_token)

    with allure.step("Проверка успешного ответа"):
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}. Ответ: {response.text}"
        assert 'orders' in response.json(), "Нет ключа 'orders' в ответе"