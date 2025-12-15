from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.grabdocs.com/login")

        # Instructions for manual login
        print("\n=== MANUAL LOGIN REQUIRED ===")
        print("1. In the browser that just opened, log in normally.")
        print("2. Complete any 2FA or extra steps.")
        print("3. Navigate to the Calendar page if needed.")
        print("4. When you can see your calendar, come back here and press ENTER.\n")

        input("Press ENTER here after you're fully logged in and on calendar...")

        context.storage_state(path="state.json")
        print("Saved authenticated state to state.json")

        browser.close()

if __name__ == "__main__":
    main()
