import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.regression
def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.navigate("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded()

    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == 1

    inventory_page.go_to_cart()
    assert cart_page.has_items()
