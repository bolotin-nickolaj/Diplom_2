import allure
from user_api import UserApi
from url import Urls
from constant import Responses as R


class TestGetOrders:
    @allure.title("Получение заказов пользователя")
    @allure.description("Получить заказы авторизированного пользователя")
    def test_receive_orders_from_an_authorized_user(self, get_data_of_new_register_user):
        api = UserApi()
        user = get_data_of_new_register_user
        login = api.post(Urls.user_login, user)
        accessToken = login.json()["accessToken"]
        orders = api.get(Urls.order, accessToken)
        assert orders.status_code == R.resp_test_get_orders_status_code1
        assert orders.json()["success"] == R.resp_test_get_orders_success

    @allure.title("Получение заказов пользователя")
    @allure.description("Получить заказы НЕ авторизированного пользователя")
    def test_receive_orders_from_an_unauthorized_user(self):
        api = UserApi()
        orders = api.get(Urls.order)
        assert orders.status_code == R.resp_test_get_orders_status_code2
        assert orders.json()["message"] == R.resp_test_get_orders_authorised
