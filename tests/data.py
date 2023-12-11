from faker import Faker


class Urls:
    url = 'https://stellarburgers.nomoreparties.site/api/'


class User:
    fake = Faker()
    name = fake.first_name()
    password = fake.password(special_chars=False)
    email = fake.email()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    payload_without_name = {
        "email": email,
        "password": password
    }
    payload_without_password = {
        "email": email,
        "name": name
    }
    payload_without_email = {
        "password": password,
        "name": name
    }
    email_mod = fake.email()
    name_mod = fake.first_name()
    password_mod = fake.password(special_chars=False)
    payload_mod = {
        "email": email_mod,
        "password": password_mod,
        "name": name_mod,
    }
