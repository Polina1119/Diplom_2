import requests
import api
import data
import allure

url = data.Urls.url
payload = data.User.payload


class TestLoginUser:

    @allure.title('Проверка логина пользователя с валидными данными')
    def test_login_user(self, prepare_user):
        api.register_user()
        with allure.step('Отправка POST запроса, используя сгенерированные данные'):
            response = requests.post(f'{url}auth/login', data=payload)
        prepare_user(payload)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200

    @allure.title('Проверка логина несуществующего пользователя')
    def test_login_non_existent_courier(self):
        with allure.step('Отправка POST запроса, используя сгенерированные данные'):
            response = requests.post(f'{url}auth/login', data=payload)

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()['message'] == "email or password are incorrect"
        with allure.step("Статус код ответа равен 401"):
            assert response.status_code == 401




