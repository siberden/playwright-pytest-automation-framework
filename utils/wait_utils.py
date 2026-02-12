from playwright.sync_api import Page

def wait_for_element(page: Page, selector: str):
    page.wait_for_selector(selector)
