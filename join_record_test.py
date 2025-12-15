from pages.calendar_page import CalendarPage
from playwright.sync_api import expect


def test_join_and_record_meeting(page):
    calendar = CalendarPage(page)

    # Open the first event in the calendar
    calendar.open_first_event()

    # Click the "Join" button to enter the meeting
    join_button = page.get_by_text("Join").first
    join_button.wait_for(timeout=15000)
    join_button.click()

    # Wait for the meeting interface to load
    record_button = page.get_by_text("Record").first
    record_button.wait_for(timeout=15000)
    record_button.click()


    page.wait_for_timeout(5000)

    # Stop the recording
    stop_button = page.get_by_text("Stop Recording").first
    stop_button.wait_for(timeout=15000)
    stop_button.click()
