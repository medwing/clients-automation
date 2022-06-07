import pytest

from test_data.login_test_data import *
from utilities.readProperties import read_config

config_values = read_config('urls')


@pytest.mark.regression
def test_regular_ats_login(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
    finally:
        ui.close()
