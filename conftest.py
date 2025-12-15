import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture(scope="session")
def BASE_URL():

    # Return the base URL from environment variable or default to the calendar URL
    return os.getenv("BASE_URL") or "https://app.grabdocs.com/calendar"


@pytest.fixture(scope="session")
def INVITEE_EMAIL():
    # Return the invitee email from environment variable
    return os.getenv("INVITEE_EMAIL")


@pytest.fixture(scope="session")
def browser():
 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        yield context
        browser.close()


@pytest.fixture
def page(browser, BASE_URL):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()
