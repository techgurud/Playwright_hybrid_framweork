from playwright.sync_api import sync_playwright

def test_navigate_to_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Navigate to the URL
        page.goto("https://www.saucedemo.com/")
        
        # Assert the page title or URL to ensure navigation was successful
        assert page.url == "https://www.saucedemo.com/"
        
        # Close the browser
        browser.close()