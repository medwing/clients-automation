import time

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
        self.navigate_to_candidates_page()
        self.navigate_to_vacancies_page()
        self.navigate_to_home_page()

    def navigate_to_candidates_page(self):
        self.wait_for_element_to_be_visible(CANDIDATE_LINK_XPATH, "xpath")
        self.click_element(CANDIDATE_LINK_XPATH, "xpath")
        assert self.is_element_present(ALL_BTN_XPATH, "xpath")

    def navigate_to_vacancies_page(self):
        self.wait_for_element_to_be_clickable(VACANCIES_LINK_XPATH, "xpath")
        self.click_element(VACANCIES_LINK_XPATH, "xpath")
        assert self.is_element_present(ADD_NEW_JOB_BTN_XPATH, "xpath")

    def navigate_to_home_page(self):
        self.wait_for_element_to_be_clickable(HOME_LINK_XPATH, "xpath")
        self.click_element(HOME_LINK_XPATH, "xpath")
        assert self.is_element_present(VIEW_ALL_CANDIDATES_BTN_ID, "id")

    def validate_candidates_page(self):
        pass

    def filter_all(self):
        self.open_national_recruiting_page()
        self.navigate_to_candidates_page()
        self.click_element(ALL_BTN_XPATH, "xpath")
        assert self.get_css_value('background-color', ALL_BTN_XPATH, "xpath") == 'rgba(33, 206, 181, 1)'
        count = int(self.get_text(ALL_FILTER_COUNT_CSS, "css"))
        # pageCount = int(self.get_element_count(PAGINATION_BTN_COUNT_CSS, "css")) - 2
        self.click_element(PAGINATION_LAST_BTN_XPATH, "xpath")
        time.sleep(3)
        candidate_count = int(self.get_element_count(CANDIDATE_COUNT_CSS, "css"))
        if count > 25:
            assert count - 25 == candidate_count

    def pagination(self):
        self.open_national_recruiting_page()
        self.navigate_to_candidates_page()
        self.click_element(ALL_BTN_XPATH, "xpath")
        assert "disabled" in self.get_attribute('class', PREVIOUS_PAGE_BTN_LIST_XPATH, "xpath")
        assert "disabled" not in self.get_attribute('class', NEXT_PAGE_BTN_LIST_XPATH, "xpath")
        assert self.get_css_value('color', PAGINATION_BTN_COUNT_CSS + ":nth-child(2) a", "css") == "rgba(19, 197, 168, 1)"
        self.click_element(NEXT_PAGE_BTN_LIST_XPATH, "xpath")
        assert self.get_css_value('color', PAGINATION_BTN_COUNT_CSS + ":nth-child(3) a", "css") == "rgba(19, 197, 168, 1)"

    def candidate_filter_dropdown(self):
        self.set_item_in_localstorage('langCode', 'en')
        self.open_national_recruiting_page()
        self.navigate_to_candidates_page()
        self.click_element(STATUS_DROPDOWN_BTN_XPATH, "xpath")
        for i in range(1, self.get_element_count(FILTER_DROPDOWN_VALUE_XPATH, "xpath")):
            print(self.get_text((FILTER_DROPDOWN_VALUE_XPATH + "[{0}]/div/div[1]").format(i), "xpath"))

