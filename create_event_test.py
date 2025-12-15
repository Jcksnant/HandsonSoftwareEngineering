from pages.calendar_page import CalendarPage
from pages.new_event_page import NewEventPage


def test_create_meeting_with_invitees_and_reminder(page, INVITEE_EMAIL):

    calendar = CalendarPage(page)

    # Open the new event creation interface
    calendar.open_new_event()

    new_event = NewEventPage(page)

    # Create a basic event with invitees and a reminder
    new_event.create_basic_event("Automation Meeting", INVITEE_EMAIL)

    body_text = page.locator("body").inner_text()
    assert "No events" not in body_text
