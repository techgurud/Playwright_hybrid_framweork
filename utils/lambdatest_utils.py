import os
from playwright.sync_api import sync_playwright

LAMBDA_TEST_USERNAME = os.getenv("LAMBDA_TEST_USERNAME")
LAMBDA_TEST_ACCESS_KEY = os.getenv("LAMBDA_TEST_ACCESS_KEY")
LAMBDA_TEST_GRID_URL = f"https://{LAMBDA_TEST_USERNAME}:{LAMBDA_TEST_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

def configure_lambda_test():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "LT:Options": {
            "platform": "Windows 10",
            "build": "Playwright Python Build",
            "name": "Playwright Python Test",
            "user": LAMBDA_TEST_USERNAME,
            "accessKey": LAMBDA_TEST_ACCESS_KEY,
            "network": True,
            "video": True,
            "console": True,
        }
    }
    return capabilities

def run_test():
    capabilities = configure_lambda_test()
    with sync_playwright() as p:
        browser = p.chromium.connect(f"wss://cdp.lambdatest.com/playwright?capabilities={capabilities}")
        page = browser.new_page()
        page.goto("https://www.example.com")
        print(page.title())
        browser.close()

if __name__ == "__main__":
    run_test()

    