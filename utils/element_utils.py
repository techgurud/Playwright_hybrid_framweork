from playwright.sync_api import Page, Locator

class ElementUtils:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, selector: str, timeout: int = 30000):
        """Clicks on an element specified by the selector."""
        self.page.locator(selector).click(timeout=timeout)

    def type_text(self, selector: str, text: str, clear: bool = True, timeout: int = 30000):
        """Types text into an input field specified by the selector."""
        locator = self.page.locator(selector)
        if clear:
            locator.fill("")
        locator.type(text, timeout=timeout)

    def get_text(self, selector: str, timeout: int = 30000) -> str:
        """Gets the text content of an element specified by the selector."""
        return self.page.locator(selector).text_content(timeout=timeout)

    def is_element_visible(self, selector: str, timeout: int = 30000) -> bool:
        """Checks if an element is visible on the page."""
        return self.page.locator(selector).is_visible(timeout=timeout)

    def is_element_enabled(self, selector: str, timeout: int = 30000) -> bool:
        """Checks if an element is enabled on the page."""
        return self.page.locator(selector).is_enabled(timeout=timeout)

    def wait_for_element(self, selector: str, timeout: int = 30000):
        """Waits for an element to be visible on the page."""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def select_dropdown_option(self, selector: str, value: str, timeout: int = 30000):
        """Selects an option from a dropdown by value."""
        self.page.locator(selector).select_option(value=value, timeout=timeout)

    def get_attribute(self, selector: str, attribute: str, timeout: int = 30000) -> str:
        """Gets the value of an attribute of an element."""
        return self.page.locator(selector).get_attribute(attribute, timeout=timeout)