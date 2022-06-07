import pytest

from test_cases.test_regular_ats_login import config_values
from test_data.login_test_data import *


@pytest.mark.regression
def test_side_navigation_bar(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.national_recruiting_page.validate_side_navigation_bar()
    finally:
        ui.close()
