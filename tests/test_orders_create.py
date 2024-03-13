import allure
from user_api import UserApi
from url import Urls
from constant import TestData


class TestOrdersCreate:
    @allure.title("Успешное создание заказа с указанием ингредиентов")
    @allure.description("Авторизированный пользователь может создать заказ")
    def test_creating_an_order_by_an_authorized_user_with_ingredients(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        login = api.post(Urls.user_login, user)
        accessToken = login.json()["accessToken"]
        order_data = {"ingredients": TestData.ingredients, "Authorization": accessToken}
        orders = api.post(Urls.order, order_data)
        assert orders.json()["success"] == True

    @allure.title("Успешное создание заказа с указанием ингредиентов")
    @allure.description("Неавторизированный пользователь тоже может создать заказ")
    def test_creating_an_order_by_an_unauthorized_user_with_ingredients(self):
        api = UserApi()
        order_data = {"ingredients": TestData.ingredients}
        orders = api.post(Urls.order, order_data)
        assert orders.json()["success"] == True

    @allure.title("Неуспешное создание заказа с неверными или отсутствующими ингредиентами")
    @allure.description("Авторизированный пользователь не может создать заказ с пустыми ингредиентами")
    def test_creating_an_order_by_an_authorized_user_without_ingredients(self, register_new_user_and_return_login_password):
        api = UserApi()
        user = {"name": register_new_user_and_return_login_password[0],
                "password": register_new_user_and_return_login_password[1],
                "email": register_new_user_and_return_login_password[2]}
        login = api.post(Urls.user_login, user)
        accessToken = login.json()["accessToken"]
        order_data = {"ingredients": None, "Authorization": accessToken}
        orders = api.post(Urls.order, order_data)
        assert orders.status_code == 400
        assert orders.json()["message"] == "Ingredient ids must be provided"


    @allure.title("Неуспешное создание заказа с неверными или отсутствующими ингредиентами")
    @allure.description("Неавторизированный пользователь не может создать заказ с неверными ингредиентами")
    def test_creating_an_order_by_an_unauthorized_user_with_wrong_ingredients(self):
        api = UserApi()
        order_data = {"ingredients": TestData.wrong_ingredients}
        orders = api.post(Urls.order, order_data)
        assert orders.status_code == 500
