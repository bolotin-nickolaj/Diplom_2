import allure

from user_api import UserApi
from url import Urls
from constant import Responses as R


class TestChangeUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Авторизованный пользователь может изменить данные своей учетки.")
    def test_changing_user_data_with_authorization(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        login = api.post(Urls.user_login, user)
        accessToken = login.json()["accessToken"]
        changed_user_data = {"name": "", "password": "", "email": ""}
        response = api.patch(Urls.user_info, changed_user_data, accessToken)
        assert response.json()["success"] == R.resp_test_user_change_success1
    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Неавторизованный пользователь НЕ может изменить данные своей учетки.")
    def test_test_changing_user_data_without_authorization(self):
        api = UserApi()
        changed_user_data = {"name": "", "password": "", "email": ""}
        response = api.patch(Urls.user_info, changed_user_data)
        assert response.json()["success"] == R.resp_test_user_change_success2
        assert response.json()["message"] == R.resp_test_user_change_authorised
