from pages.calendar_page import CalendarPage


def test_meeting_assets(page):

    # Initialize the CalendarPage object
    calendar = CalendarPage(page)
    
    # Open the first event in the calendar
    calendar.open_first_event()

    assets_button = page.get_by_text("Assets").first
    assets_button.wait_for(timeout=15000)
    assets_button.click()

    assets = page.locator("div.asset-item")
    assert assets.count() > 0, "No assets found for the meeting."
