from page_objects.dashboard.dashboard_page import DashboardPage
from page_objects.login.login_page import LoginPage
from page_objects.national_recruiting.national_recruiting_page import NationalRecruitingPage
from utilities.myselenium_driver import SeleniumDriver


class UI:

    def __init__(self, driver):
        # Initialize all the page object classes below
        self.driver = driver
        self.implicit_wait = self.driver.implicitly_wait(10)
        self.common_helpers = SeleniumDriver(self)
        self.login_page = LoginPage(self)
        self.dashboard_page = DashboardPage(self)
        self.national_recruiting_page = NationalRecruitingPage(self)

    # def open(self):
    #     self.driver.get(self.url)

    def destroy(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.close()
