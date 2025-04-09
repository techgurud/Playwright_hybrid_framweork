import openpyxl
import pytest
from page_objects.home_page import home_page
from playwright.sync_api import Page


class Login_page:
    def __init__(self, page):
        self.page = page
        username = page.locator("[data-test=\"username\"]")
        password = page.locator("[data-test=\"password\"]")
        login_button = page.locator("[data-test=\"login-button\"]")
        error = page.locator("[data-test=\"error\"]")
        title = page.locator("[data-test=\"title\"]")
    
    def login(self, username, password, login_button):
        username.fill(username)
        password.fill(password)
        login_button.click()
        return home_page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
    