import allure

from user_api import UserApi
from url import Urls
from constant import Responses as R


class TestLogin:
    @allure.title("Успешный логин под существующим пользователем.")
    @allure.description("Логин пользователя.")
    def test_user_successful_login(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        response = api.post(Urls.user_login, user)
        assert response.status_code == R.resp_test_user_login_status_code1
        assert response.json()["success"] == R.resp_test_user_login_success

    @allure.title("Безуспешный логин пользователя с неуказанным паролем.")
    @allure.description("Попытка логина с неверными данными.")
    def test_unsuccessful_login_with_wrong_data(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": " ",
                "email": register_new_user_and_return_login_password[2]}
        response = api.post(Urls.user_login, user)
        assert response.status_code == R.resp_test_user_login_status_code2
        assert response.json()["message"] == R.resp_test_user_login_message
