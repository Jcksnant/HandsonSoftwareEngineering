from playwright.sync_api import Page
from .base_page import BasePage


class NewEventPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def create_basic_event(self, title: str, invitee_email: str):

        # Wait for the new event page to load
        self.page.get_by_text("Create New Event").wait_for(timeout=15000)

        # Fill in the event details
        self.page.get_by_placeholder("Team Meeting, Client Call, etc.").fill(title)

        #Adding details to the event
        self.page.get_by_placeholder("Add details about the event...").fill(
            "Automation test event created by Playwright.")

        # Fill in the location
        self.page.get_by_placeholder("Conference Room A").fill("Automation Test Room")

        # Add invitee email
        self.page.get_by_placeholder("email@example.com").fill(invitee_email)

        participants_row = self.page.locator(
            "div:has(input[placeholder='Name (optional)'])"
        )
        add_button = participants_row.locator("button").last
        add_button.click()

        # Set a reminder
        self.page.get_by_role("button", name="15 min before").click()

        #Click the create event button
        create_button = self.page.get_by_text("Create Event").first
        create_button.wait_for(timeout=15000)
        create_button.click()