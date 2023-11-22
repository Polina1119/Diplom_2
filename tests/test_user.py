import requests
from conftest import url
from data import *
import allure


class TestUser:

    @allure.title('Проверка изменения данных пользователя c авторизацией')
    def test_patch_user_with_authorization(self, prepare_user):
        with allure.step('Генерация данных и регистрация пользователя'):
            payload = {
                "email": email,
                "password": password,
                "name": name
            }
            response_register = requests.post(f'{url}auth/register', data=payload)
        token = response_register.json()['accessToken']
        with allure.step('Отправка PATCH запроса, используя заголовки'):
            with allure.step('Генерация данных для изменения'):
                payload_mod = {
                    "email": email,
                    "password": password,
                    "name": name
                }
            response = requests.patch(f'{url}auth/user', data=payload_mod, headers={"Authorization": token})
        prepare_user(payload)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_patch_user_without_authorization(self):
        with allure.step('Отправка PATCH запроса'):
            with allure.step('Генерация данных и регистрация пользователя'):
                payload = {
                    "email": email,
                    "password": password,
                    "name": name
                }
            response = requests.patch(f'{url}auth/user', data=payload)

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()['message'] == "You should be authorised"
        with allure.step("Статус код ответа равен 401"):
            assert response.status_code == 401




