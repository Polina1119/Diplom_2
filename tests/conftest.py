import pytest
import requests
import data

url = data.Urls.url
token = None


@pytest.fixture(scope='function')
def prepare_user():

    def _prepare_user(payload):
        global token
        response = requests.post(f'{url}auth/login', data=payload)
        token = response.json()['accessToken']
        return response

    yield _prepare_user
    requests.delete(f'{url}auth/user', headers={"Authorization":token})
