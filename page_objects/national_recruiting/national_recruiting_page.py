from page_objects.dashboard.dashboard_page_locator import NATIONAL_RECRUITING_BTN_XPATH
from page_objects.national_recruiting.national_recruiting_page_locator import *
from utilities.myselenium_driver import SeleniumDriver


class NationalRecruitingPage(SeleniumDriver):
    def __init__(self, ui):
        super().__init__(ui)
        self.driver = ui.driver

    def open_national_recruiting_page(self):
        self.wait_for_element_to_be_visible(NATIONAL_RECRUITING_BTN_XPATH, "xpath")
        self.click_element(NATIONAL_RECRUITING_BTN_XPATH, "xpath")

    def validate_side_navigation_bar(self):
        self.open_national_recruiting_page()
        self.wait_for_element_to_be_visible(CANDIDATE_LINK_XPATH, "xpath")
        self.click_element(CANDIDATE_LINK_XPATH, "xpath")
        assert self.is_element_present(ALL_BTN_XPATH, "xpath")

        self.wait_for_element_to_be_clickable(VACANCIES_LINK_XPATH, "xpath")
        self.click_element(VACANCIES_LINK_XPATH, "xpath")
        assert self.is_element_present(ADD_NEW_JOB_BTN_XPATH, "xpath")

        self.wait_for_element_to_be_clickable(HOME_LINK_XPATH, "xpath")
        self.click_element(HOME_LINK_XPATH, "xpath")
        assert self.is_element_present(VIEW_ALL_CANDIDATES_BTN_ID, "id")
