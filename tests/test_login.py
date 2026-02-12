import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authentication")
@allure.story("Valid Login")
@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded()


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.navigate("https://www.saucedemo.com")
    login_page.login("locked_out_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()
