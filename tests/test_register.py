import requests
from conftest import url
import data
import allure

payload = data.User.payload


class TestRegisterUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_create_user(self, prepare_user):
        with allure.step('Отправка POST запроса'):
            response = requests.post(f'{url}auth/register', data=payload)
        prepare_user(payload)

        with allure.step("Запрос отправлен, посмотрим тело ответа"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"


    @allure.title('Проверка создания существующего пользователя')
    def test_create_existing_user(self, prepare_user):
        with allure.step('Отправка двух POST запросов, используя сгенерированные данные'):
            response = requests.post(f'{url}auth/register', data=payload)
            response2 = requests.post(f'{url}auth/register', data=payload)
        r = response2.json()
        prepare_user(payload)

        with allure.step("Проверка сообщения об ошибке"):
            assert r['message'] == "User already exists"
        with allure.step("Статус код ответа равен 403"):
            assert response2.status_code == 403, f"Неверный код ответа, получен {response.status_code}"

    @allure.title('Проверка создания пользователя без обязательного поля')
    def test_create_user_without_field(self):
        with allure.step('Генерация данных'):
            payload_without_name = data.User.payload_without_name
            payload_without_password = data.User.payload_without_password
            payload_without_email = data.User.payload_without_email
        with allure.step('Отправка POST запросов, используя сгенерированные данные'):
            response = requests.post(f'{url}auth/register', data=payload_without_name)
            response2 = requests.post(f'{url}auth/register', data=payload_without_password)
            response3 = requests.post(f'{url}auth/register', data=payload_without_email)
        r = response.json()
        r2 = response2.json()
        r3 = response3.json()

        with allure.step("Проверка сообщения об ошибке"):
            assert r['message'] == "Email, password and name are required fields"
            assert r2['message'] == "Email, password and name are required fields"
            assert r3['message'] == "Email, password and name are required fields"
        with allure.step("Статус код ответа равен 403"):
            assert response.status_code == 403, f"Неверный код ответа, получен {response.status_code}"
            assert response2.status_code == 403, f"Неверный код ответа, получен {response.status_code}"
            assert response3.status_code == 403, f"Неверный код ответа, получен {response.status_code}"