from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = ".cart_item"

    def has_items(self):
        return self.is_visible(self.CART_ITEM)
