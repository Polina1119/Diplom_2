import requests
from conftest import url
from data import *
import allure


class TestOrders:

    @allure.title('Проверка создания заказа без авторизации')
    def test_orders_without_authorization(self):
        payload = {
            "ingredients":
                [
                    "61c0c5a71d1f82001bdaaa6d"
                ]
            }
        with allure.step('Отправка POST запроса'):
            response = requests.post(f'{url}orders', data=payload)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200

    @allure.title('Проверка создания заказа с авторизацией')
    def test_orders_with_authorization(self, prepare_user):
        with allure.step('Генерация данных и регистрация пользователя'):
            payload_user = {
                "email": email,
                "password": password,
                "name": name
            }
            response_register = requests.post(f'{url}auth/register', data=payload_user)
        token = response_register.json()['accessToken']
        payload = {
            "ingredients":
                [
                    "61c0c5a71d1f82001bdaaa6d"
                ]
        }
        with allure.step('Отправка POST запроса'):
            response = requests.post(f'{url}orders', data=payload, headers={"Authorization": token})
        prepare_user(payload_user)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_orders_without_ingredients(self):
        payload = {
            "ingredients":
                []
        }
        with allure.step('Отправка POST запроса'):
            response = requests.post(f'{url}orders', data=payload)

        with allure.step("Проверка, что неуспешный запрос возвращает false"):
            assert response.json()['success'] == False
        with allure.step("Статус код ответа равен 400"):
            assert response.status_code == 400

    @allure.title('Проверка создания заказа с некорректным хешем ингредиентов')
    def test_orders_with_incorrect_hash(self, prepare_user):
        with allure.step('Генерация данных и регистрация пользователя'):
            payload_user = {
                "email": email,
                "password": password,
                "name": name
            }
            response_register = requests.post(f'{url}auth/register', data=payload_user)
        token = response_register.json()['accessToken']
        payload = {
            "ingredients":
                [
                    "61c0c5a7f82001bdaaa6d"
                ]
        }
        with allure.step('Отправка POST запроса'):
            response = requests.post(f'{url}orders', data=payload, headers={"Authorization": token})
        prepare_user(payload_user)

        with allure.step("Статус код ответа равен 500"):
            assert response.status_code == 500

    @allure.title('Проверка получения заказов без авторизации')
    def test_orders_without_authorization(self):
        with allure.step('Отправка GET запроса'):
            response = requests.get(f'{url}orders')

        with allure.step("Проверка, что успешный запрос возвращает false"):
            assert response.json()['success'] == False
        with allure.step("Статус код ответа равен 401"):
            assert response.status_code == 401

    @allure.title('Проверка получения заказов с авторизацией')
    def test_orders_with_authorization(self, prepare_user):
        with allure.step('Генерация данных и регистрация пользователя'):
            payload_user = {
                "email": email,
                "password": password,
                "name": name
            }
            response_register = requests.post(f'{url}auth/register', data=payload_user)
        token = response_register.json()['accessToken']
        with allure.step('Отправка GET запроса'):
            response = requests.get(f'{url}orders', headers={"Authorization": token})
        prepare_user(payload_user)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200