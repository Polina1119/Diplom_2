import allure
import requests
import data
from faker import Faker

url = data.Urls.url
payload = data.User.payload


def register_user():
    with allure.step('Генерация данных и регистрация пользователя'):
        response = requests.post(f'{url}auth/register', data=payload)

    return response
