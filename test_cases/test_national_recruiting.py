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


@pytest.mark.regression
def test_all_filter_candidates(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.national_recruiting_page.filter_all()
    finally:
        ui.close()


@pytest.mark.regression
def test_candidate_pagination(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.national_recruiting_page.pagination()
    finally:
        ui.close()


@pytest.mark.regression
def test_candidate_filter_dropdown_check(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.national_recruiting_page.candidate_filter_dropdown()
    finally:
        ui.close()


@pytest.mark.regression
def test_candidate_cards(ui):
    try:
        ui.driver.get(config_values['regular_ats_url'])
        ui.login_page.login(regular_ats_username, regular_ats_password)
        ui.national_recruiting_page.validate_candidates_card()
    finally:
        ui.close()
