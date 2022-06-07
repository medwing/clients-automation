from page_objects.dashboard.dashboard_page_locator import *
from page_objects.national_recruiting.national_recruiting_page_locator import HOME_LINK_XPATH
from utilities.myselenium_driver import SeleniumDriver


class DashboardPage(SeleniumDriver):
    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver

    def validate_national_recruiting_btn(self):
        self.wait_for_element_to_be_visible(NATIONAL_RECRUITING_BTN_XPATH, "xpath")
        self.click_element(NATIONAL_RECRUITING_BTN_XPATH, "xpath")
        self.wait_for_element_to_be_visible(HOME_LINK_XPATH, "xpath")
        assert self.get_current_url() == "https://clients.mwngdev.com/home"
