import allure
import requests

from user_api import UserApi
from url import Urls
from constant import Responses as R


class TestUser:
    @allure.title("Успешное создание уникального пользователя.")
    @allure.description("Пользователь создан.")
    def test_create_user_success(self, register_new_user_and_return_login_password):
        assert len(register_new_user_and_return_login_password) > R.resp_test_user_create_count
    @allure.title("Создание пользователя, который уже зарегистрирован.")
    @allure.description("Нельзя создать двух одинаковых пользователей.")
    def test_create_user_with_same_parameters_is_impossible(self, register_new_user_and_return_login_password):
        api = UserApi()
        data = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        response = requests.post(url=Urls.user_create, data=data)
        assert response.status_code == 403
        assert response.json()['message'] == R.resp_test_user_create_exists
    @allure.title("Создание пользователя и не заполнить одно из обязательных полей.")
    @allure.description("Нельзя создать пользователя с пустыми параметрами.")
    def test_create_user_with_empty_parameters_is_impossible(self):
        api = UserApi()
        data = {"name": "", "password": "", "email": ""}
        response = requests.post(url=Urls.user_create, data=data)
        assert response.status_code == 403
        assert response.json()['message'] == R.resp_test_user_create_required
