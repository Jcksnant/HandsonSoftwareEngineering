# Playwright Calendar Automation Project

##Overview

This project is an end-to-end automated testing framework built with **Playwright (Python)** and **pytest** to validate core calendar and meeting functionality in the GrabDocs.

The goal of this project is to demonstrate:
- Browser-based UI automation
- Page Object Model design
- Authentication handling with 2FA
- Realistic testing constraints for time-based meeting features
- Automated test reporting

---

##Features Tested

The test suite validates the following objectives:

##Calendar
- Switch between months in the calendar view
- Verify calendar updates correctly

##Create Meeting
- Create a new meeting event
- Fill event title, description, location, and participants
- Add email invitees
- Configure reminders
- Submit the event successfully

##Join & Record Meeting *(Conditional)*
- Open an existing meeting
- Join the meeting (only if its available)
- Start and stop recording (only if meeting allows it)

> **Note:** Join and Record features may not be available if the meeting is scheduled in the future or does not support live sessions. These tests are conditionally skipped when the UI does not expose the required buttons.

## Tech Stack

- **Python 3.13**
- **Playwright (sync API)**
- **pytest**
- **pytest-html** (HTML reports)
- **python-dotenv** (environment configuration)

---

## Project Structure

```text
PlaywrightCalenderProject/
├── conftest.py                 # Pytest fixtures & session setup
├── save_auth_state.py          # One-time manual login + 2FA capture
├── state.json                  # Stored authenticated browser session
├── pages/
│   ├── __init__.py
│   ├── base_page.py            # Shared helper methods
│   ├── calendar_page.py        # Calendar interactions
│   └── new_event_page.py       # Create Event form logic
├── tests/
│   ├── create_event_test.py
│   ├── join_record_test.py
│   ├── month_switch_test.py
│   └── test_assets.py
├── requirements.txt
└── README.md
