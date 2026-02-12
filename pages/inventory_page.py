from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER = ".inventory_list"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"

    def is_loaded(self):
        return self.is_visible(self.INVENTORY_CONTAINER)

    def add_first_product_to_cart(self):
        self.page.locator(".inventory_item button").first.click()

    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_ICON)
