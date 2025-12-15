from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Basic wrapper methods
    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def wait_for_visible(self, selector: str):
        return self.page.wait_for_selector(selector)

    def expect_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()
