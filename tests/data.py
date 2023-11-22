from faker import Faker

url = 'https://stellarburgers.nomoreparties.site/api/'

fake = Faker()
name = fake.first_name()
password = fake.password(special_chars=False)
email = fake.email()
