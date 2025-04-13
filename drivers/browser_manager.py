from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self, browser_type="chromium", headless=True):
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self):
        self.playwright = sync_playwright().start()
        if self.browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def get_page(self):
        if not self.page:
            raise RuntimeError("Browser is not started. Call start_browser() first.")
        return self.page

    def stop_browser(self):
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

# Example usage:
# manager = BrowserManager(browser_type="chromium", headless=False)
# manager.start_browser()
# page = manager.get_page()
# page.goto("https://example.com")
# manager.stop_browser()