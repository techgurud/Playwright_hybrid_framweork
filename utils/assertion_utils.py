from playwright.sync_api import Page

def assert_text_equals(actual_text: str, expected_text: str, message: str = ""):
    """
    Asserts that two strings are equal.
    """
    assert actual_text == expected_text, message or f"Expected '{expected_text}', but got '{actual_text}'"

def assert_element_visible(page: Page, selector: str, message: str = ""):
    """
    Asserts that an element is visible on the page.
    """
    element = page.query_selector(selector)
    assert element and element.is_visible(), message or f"Element with selector '{selector}' is not visible"

def assert_element_not_visible(page: Page, selector: str, message: str = ""):
    """
    Asserts that an element is not visible on the page.
    """
    element = page.query_selector(selector)
    assert not (element and element.is_visible()), message or f"Element with selector '{selector}' is visible"

def assert_element_contains_text(page: Page, selector: str, expected_text: str, message: str = ""):
    """
    Asserts that an element contains the expected text.
    """
    element = page.query_selector(selector)
    assert element, message or f"Element with selector '{selector}' not found"
    actual_text = element.text_content()
    assert expected_text in actual_text, message or f"Expected text '{expected_text}' not found in element text '{actual_text}'"

def assert_url_equals(page: Page, expected_url: str, message: str = ""):
    """
    Asserts that the current page URL matches the expected URL.
    """
    actual_url = page.url
    assert actual_url == expected_url, message or f"Expected URL '{expected_url}', but got '{actual_url}'"

def assert_title_equals(page: Page, expected_title: str, message: str = ""):
    """
    Asserts that the page title matches the expected title.
    """
    actual_title = page.title()
    assert actual_title == expected_title, message or f"Expected title '{expected_title}', but got '{actual_title}'"

def assert_element_count(page: Page, selector: str, expected_count: int, message: str = ""):
    """
    Asserts that the number of elements matching the selector equals the expected count.
    """
    elements = page.query_selector_all(selector)
    actual_count = len(elements)
    assert actual_count == expected_count, message or f"Expected {expected_count} elements, but found {actual_count}"