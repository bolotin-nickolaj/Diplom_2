import allure
import pytest

from user_api import UserApi
from url import Urls


class TestLogin:
    @allure.title("Успешный логин под существующим пользователем.")
    @allure.description("Логин пользователя.")
    def test_user_successful_login(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        response = api.post(Urls.user_login, user)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Безуспешный логин пользователя с неуказанным паролем.")
    @allure.description("Попытка логина с неверными данными.")
    def test_unsuccessful_login_with_wrong_data(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": " ",
                "email": register_new_user_and_return_login_password[2]}
        response = api.post(Urls.user_login, user)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
