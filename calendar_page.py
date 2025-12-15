from playwright.sync_api import Page
from .base_page import BasePage


class CalendarPage(BasePage):
    NEXT_BUTTON = "button:has-text('Next')"
    BACK_BUTTON = "button:has-text('Back')"

    def __init__(self, page: Page):
        super().__init__(page)

    # Navigate to the new event creation page
    def open_new_event(self):
        self.page.goto("https://app.grabdocs.com/calendar/create")
        self.page.get_by_placeholder("Team Meeting, Client Call, etc.").wait_for(
            timeout=15000
        )

    def switch_next_month(self):
        self.click(self.NEXT_BUTTON)

    def switch_previous_month(self):
        self.click(self.BACK_BUTTON)

    def open_first_event(self):
        self.page.goto("https://app.grabdocs.com/calendar")

        event = self.page.get_by_text("Automation Meeting").first
        event.wait_for(timeout=15000)
        event.click()
