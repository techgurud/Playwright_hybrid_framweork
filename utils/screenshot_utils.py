import os
from playwright.sync_api import Page

class ScreenshotUtils:
    def __init__(self, screenshot_dir: str = "screenshots"):
        self.screenshot_dir = screenshot_dir
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, page: Page, name: str):
        """
        Captures a screenshot of the current page.

        :param page: Playwright Page object
        :param name: Name of the screenshot file (without extension)
        """
        file_path = os.path.join(self.screenshot_dir, f"{name}.png")
        page.screenshot(path=file_path)
        print(f"Screenshot saved at: {file_path}")