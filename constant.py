class Constants:
    header = {"accept": "application/json", "Content-Type": "application/json"}

class TestData:
    ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    wrong_ingredients = ["09098098", "456876554"]

class Responses:
    resp_test_get_orders_authorised = "You should be authorised"
    resp_test_get_orders_success = True
    resp_test_get_orders_status_code1 = 200
    resp_test_get_orders_status_code2 = 401

    resp_test_orders_create_ingredient = "Ingredient ids must be provided"
    resp_test_orders_create_success1 = True
    resp_test_orders_create_success2 = True
    resp_test_orders_create_status_code1 = 400
    resp_test_orders_create_status_code2 = 500

    resp_test_user_change_success1 = True
    resp_test_user_change_success2 = False
    resp_test_user_change_authorised = "You should be authorised"

    resp_test_user_create_count = 0
    resp_test_user_create_exists = "User already exists"
    resp_test_user_create_required = "Email, password and name are required fields"
    resp_test_user_create_status_code1 = 403
    resp_test_user_create_status_code2 = 403

    resp_test_user_login_success = True
    resp_test_user_login_status_code1 = 200
    resp_test_user_login_message = "email or password are incorrect"
    resp_test_user_login_status_code2 = 401

