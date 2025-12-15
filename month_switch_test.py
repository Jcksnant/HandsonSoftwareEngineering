from pages.calendar_page import CalendarPage
from playwright.sync_api import expect


def test_switch_month(page):
    calendar = CalendarPage(page)

    month_label = page.locator("text=/\\d{4}/").first

    expect(month_label).to_be_visible()

    old_text = month_label.inner_text()

    calendar.switch_next_month()
    expect(month_label).not_to_have_text(old_text)

    calendar.switch_previous_month()
    expect(month_label).to_have_text(old_text)
