from playwright.sync_api import sync_playwright

# Playwright utilities (e.g., setup browser, take screenshots, etc.)
def setup_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return browser, context, page

def take_screenshot(page, path):
    page.screenshot(path=path)

def close_browser(browser):
    browser.close()

# Test utilities (e.g., assert functions, etc.)
def assert_equal(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"

def assert_not_equal(actual, expected):
    assert actual != expected, f"Expected {expected}, but got {actual}"

def assert_true(actual):
    assert actual, f"Expected True, but got {actual}"

def assert_false(actual):
    assert not actual, f"Expected False, but got {actual}"

def assert_in(substring, string):
    assert substring in string, f"Expected '{substring}' to be in '{string}'"

def assert_not_in(substring, string):
    assert substring not in string, f"Expected '{substring}' to not be in '{string}'"

def assert_is_instance(obj, cls):
    assert isinstance(obj, cls), f"Expected {obj} to be an instance of {cls}"

def assert_not_is_instance(obj, cls):
    assert not isinstance(obj, cls), f"Expected {obj} to not be an instance of {cls}"

def assert_raises(exception, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exception:
        return
    assert False, f"Expected {exception} to be raised, but it was not"

def assert_not_raises(exception, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exception:
        assert False, f"Expected {exception} to not be raised, but it was"
    return

