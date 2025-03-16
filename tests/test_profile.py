from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from tools.locators import profile_name_input, profile_login_input, profile_password_input, sticky_bar_logo, \
    sticky_bar_constructor, sticky_bar_open_profile_button
from tools.functions import login

def test_open_profile_page_by_authorized_user(main_page, profile_page, existing_user):

    driver = webdriver.Chrome()

    login(driver, existing_user)

    driver.find_element(By.XPATH, sticky_bar_open_profile_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, profile_page.header)))

    assert driver.current_url == profile_page.url

    assert driver.find_element(By.XPATH, profile_name_input).get_attribute("value") == existing_user.name
    assert driver.find_element(By.XPATH, profile_login_input).get_attribute("value") == existing_user.email
    assert driver.find_element(By.XPATH, profile_password_input).get_attribute("value") == '*****'

    driver.quit()

@pytest.mark.parametrize('navigate_to_main_page', [sticky_bar_logo, sticky_bar_constructor])
def test_navigate_to_main_page_from_profile(main_page, profile_page, existing_user, navigate_to_main_page):

    driver = webdriver.Chrome()

    login(driver, existing_user)

    driver.find_element(By.XPATH, sticky_bar_open_profile_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, profile_page.header)))

    driver.find_element(By.XPATH, navigate_to_main_page).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.header)))

    assert driver.current_url == main_page.url

    driver.quit()
