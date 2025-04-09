from page_objects.login_page import Login_page
import openpyxl
import pytest
from playwright.sync_api import Page

class Home_page:
    def __init__(self, page):
        self.page = page
        title = page.locator("[data-test=\"title\"]")
        add_to_cart = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        cart = page.locator("[data-test=\"shopping_cart_container\"]")
        checkout = page.locator("[data-test=\"checkout\"]")
        remove = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def validate_page_title(self, title):
        assert self.page.title() == title, f"Expected title: {title}, but got: {self.page.title()}"

    def is_dashboard_displayed(self, title):   
        self.validate_page_title(title)
        assert self.page.locator("[data-test=\"title\"]").is_visible(), "Dashboard is not displayed"
        return True
    
