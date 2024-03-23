import pytest
import requests
import random
import string
from url import Urls

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    name = generate_random_string(10)
    password = generate_random_string(10)
    email = f'{name}@testmail.ru'

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(url=Urls.user_create, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 200:
        login_pass.append(name)
        login_pass.append(password)
        login_pass.append(email)

    # возвращаем список
    return login_pass

@pytest.fixture
def get_data_of_new_register_user(register_new_user_and_return_login_password):
    user = {"name": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1],
            "email": register_new_user_and_return_login_password[2]}
    return user

@pytest.fixture
def get_wrong_data_of_new_register_user(register_new_user_and_return_login_password):
    user = {"name": register_new_user_and_return_login_password[0],
            "password": " ",
            "email": register_new_user_and_return_login_password[2]}
    return user
