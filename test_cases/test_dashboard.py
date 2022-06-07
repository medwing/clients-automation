import pytest

from test_cases.test_regular_ats_login import config_values
from test_data.login_test_data import *


@pytest.mark.regression
def test_national_recruiting_link(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.dashboard_page.validate_national_recruiting_btn()
    finally:
        ui.close()
