import pytest
from playwright.sync_api import sync_playwright
from page_objects.login_page import Login_Page
from page_objects.home_page import Home_Page
from playwright.sync_api import Page

def login_test(page):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        login_page = Login_Page(page)
        login_page.navigate()
        login_page.username.fill("standard_user")
        login_page.password.fill("secret_sauce")
        login_page.login_button.click()
        home_page = Home_Page(page)
        home_page.validate_page_title("Swag Labs")
        home_page.is_dashboard_displayed("Swag Labs")
        browser.close()
 

