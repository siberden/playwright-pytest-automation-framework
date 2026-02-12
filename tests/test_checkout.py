import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from db.db_client import DBClient

@allure.feature("Checkout")
@allure.story("Complete Purchase Flow")
@pytest.mark.regression
def test_checkout_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    db = DBClient()

    login_page.navigate("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    checkout_page.start_checkout()
    checkout_page.fill_information("Berkuk", "Karacay", "07000")
    checkout_page.finish_order()

    assert checkout_page.is_order_complete()

    db.insert_order("Berkuk")
    assert db.order_exists("Berkuk")
