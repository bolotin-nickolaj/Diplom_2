import allure

from user_api import UserApi
from url import Urls
from constant import Responses as R


class TestLogin:
    @allure.title("Успешный логин под существующим пользователем.")
    @allure.description("Логин пользователя.")
    def test_user_successful_login(self, get_data_of_new_register_user):
        api = UserApi()
        user = get_data_of_new_register_user
        response = api.post(Urls.user_login, user)
        assert response.status_code == R.resp_test_user_login_status_code1
        assert response.json()["success"] == R.resp_test_user_login_success

    @allure.title("Безуспешный логин пользователя с неуказанным паролем.")
    @allure.description("Попытка логина с неверными данными.")
    def test_unsuccessful_login_with_wrong_data(self, get_wrong_data_of_new_register_user):
        api = UserApi()
        user = get_wrong_data_of_new_register_user
        response = api.post(Urls.user_login, user)
        assert response.status_code == R.resp_test_user_login_status_code2
        assert response.json()["message"] == R.resp_test_user_login_message
