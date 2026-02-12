class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str):
        return self.page.locator(selector).is_visible()

