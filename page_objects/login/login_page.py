from page_objects.dashboard.dashboard_page_locator import LOGOUT_BTN_CSS
from page_objects.login.login_page_locator import *
from utilities.myselenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver

    def login(self, username, password):
        self.wait_for_element_to_be_visible(EMAIL_XPATH, "xpath")
        self.send_keys(username, EMAIL_XPATH, "xpath")
        self.send_keys(password, PASSWORD_XPATH, "xpath")
        self.click_element(LOGIN_BTN_XPATH, "xpath")
        self.wait_for_element_to_be_visible(LOGOUT_BTN_CSS, "css")
