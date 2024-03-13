import allure
from user_api import UserApi
from url import Urls


class TestGetOrders:
    @allure.title("Получение заказов пользователя")
    @allure.description("Получить заказы авторизированного пользователя")
    def test_receive_orders_from_an_authorized_user(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        login = api.post(Urls.user_login, user)
        accessToken = login.json()["accessToken"]
        orders = api.get(Urls.order,accessToken)
        assert orders.status_code == 200
        assert orders.json()["success"] == True

    @allure.title("Получение заказов пользователя")
    @allure.description("Получить заказы НЕ авторизированного пользователя")
    def test_receive_orders_from_an_unauthorized_user(self):
        api = UserApi()
        orders = api.get(Urls.order)
        assert orders.status_code == 401
        assert orders.json()["message"] == "You should be authorised"
