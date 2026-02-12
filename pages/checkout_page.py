from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_BUTTON = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_information(self, first, last, zip_code):
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.ZIP, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)
