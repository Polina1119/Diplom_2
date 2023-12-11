import requests
import api
import data
import allure


payload = data.User.payload
url = data.Urls.url


class TestUser:

    @allure.title('Проверка изменения данных пользователя c авторизацией')
    def test_patch_user_with_authorization(self, prepare_user):
        response_register = api.register_user()
        token = response_register.json()['accessToken']
        with allure.step('Отправка PATCH запроса, используя заголовки'):
            payload_mod = data.User.payload_mod
            response = requests.patch(f'{url}auth/user', data=payload_mod, headers={"Authorization": token})
        prepare_user(payload_mod)

        with allure.step("Проверка, что успешный запрос возвращает true"):
            assert response.json()['success'] == True
        with allure.step("Статус код ответа равен 200"):
            assert response.status_code == 200

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_patch_user_without_authorization(self):
        api.register_user()
        with allure.step('Отправка PATCH запроса'):
            response = requests.patch(f'{url}auth/user', data=payload)

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()['message'] == "You should be authorised"
        with allure.step("Статус код ответа равен 401"):
            assert response.status_code == 401




