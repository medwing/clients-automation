HOME_LINK_XPATH = "//a[@href='home']"
CANDIDATE_LINK_XPATH = "//a[@href='permanent']"
VACANCIES_LINK_XPATH = "//a[@href='jobs']"

# HOME PAGE
VIEW_ALL_CANDIDATES_BTN_ID = "gtm_tracking_home_view_candidates"

# CANDIDATES PAGE
ALL_BTN_XPATH = "//div[@id='candidates-filter']/span/div[1]/div"
ALL_FILTER_COUNT_CSS = "div[data-cy-tab-button*='Alle'] h3:nth-child(2)"
CANDIDATE_COUNT_CSS = ".ant-table-tbody>tr"
PAGINATION_BTN_COUNT_CSS = ".ant-table-pagination-center li"
PAGINATION_LAST_BTN_XPATH = "//li[contains(@class, 'ant-pagination-next')]/button/../preceding-sibling::li[1]"
FILTER_DROPDOWN_VALUE_XPATH = "//body//ul[contains(@class, 'ant-dropdown-menu-vertical')]/li"
SUCCESS_BTN_XPATH = "//div[@id='candidates-filter']/span/div[3]/div"
REJECTED_BTN_XPATH = "//div[@id='candidates-filter']/span/div[4]/div"
STATUS_DROPDOWN_BTN_XPATH = "//div[@id='candidates-filter']/span/div[2]/button/div/div[2]"
STATUS_LABEL_XPATH = "//div[@id='candidates-filter']//button[contains(@class, 'ant-dropdown-trigger')]//h3[1]"
STATUS_COUNT_XPATH = "//div[@id='candidates-filter']//button[contains(@class, 'ant-dropdown-trigger')]//h3[2]"
SEARCH_TEXT_FIELD = "//input[@name='textSearch']"
START_DATE_XPATH = "//div[contains(@class, 'ant-picker-range')]/div[1]"
END_DATE_XPATH = "//div[contains(@class, 'ant-picker-range')]/div[3]"
FROM_DATE_XPATH = "//div[@class='ant-picker-panels']/div[1]//td[contains(@class, 'in-view')]//div[text()='{0}']"
TO_DATE_XPATH = "//div[@class='ant-picker-panels']/div[2]//td[contains(@class, 'in-view')]//div[text()='{0}']"
POSITION_DROPDOWN_XPATH = "//div[@id='filter-wrapper-position']/button"
POSITION_SEARCH_TEXT_FIELD_XPATH = "//ul[contains(@class, 'ant-dropdown-menu')]//input"
POSITION_SEARCH_BTN_XPATH = "//ul[contains(@class, 'ant-dropdown-menu')]//button[1]"
POSITION_CLEAR_TEXT_BTN_XPATH = "//ul[contains(@class, 'ant-dropdown-menu')]//button[2]"
FACILITY_DROPDOWN_XPATH = "//div[@id='filter-wrapper-facility']/button"
FACILITY_SEARCH_TEXT_FIELD_XPATH = "//div[@id='filter-wrapper-facility']//input"
FACILITY_SEARCH_BTN_XPATH = "//div[@id='filter-wrapper-facility']//ul//button[1]"
FACILITY_CLEAR_TEXT_BTN_XPATH = "//div[@id='filter-wrapper-facility']//ul//button[2]"
PREVIOUS_PAGE_BTN_XPATH = "//li[contains(@class, 'ant-pagination-prev')]/button"
NEXT_PAGE_BTN_XPATH = "//li[contains(@class, 'ant-pagination-next')]/button"
PREVIOUS_PAGE_BTN_LIST_XPATH = "//li[contains(@class, 'ant-pagination-prev')]"
NEXT_PAGE_BTN_LIST_XPATH = "//li[contains(@class, 'ant-pagination-next')]"
VIEW_FIRST_CANDIDATE_CARD_ID = "first-introduction-link"

# VACANCIES PAGE
ADD_NEW_JOB_BTN_XPATH = "//div[@id='job-create-button']/button"
LOCATION_DROPDOWN_XPATH = "//div[@id='job-create-button']//input"
GENERAL_SETTINGS_LINK_XPATH = "job-facility-settings"
