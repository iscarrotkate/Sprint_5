from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from tools.locators import sticky_bar_open_profile_button, main_enter_to_account_button, registration_login_button, \
    recovery_login_button
from tools.functions import login, password_generator


@pytest.mark.parametrize(
    'page, login_button',
    [
        ['https://stellarburgers.nomoreparties.site', sticky_bar_open_profile_button],
        ['https://stellarburgers.nomoreparties.site', main_enter_to_account_button],
        ['https://stellarburgers.nomoreparties.site/register', registration_login_button],
        ['https://stellarburgers.nomoreparties.site/forgot-password', recovery_login_button]
    ]
)
def test_open_login_form_by_unauthorized_user(authorization_page, page, login_button):

    driver = webdriver.Chrome()
    driver.get(page)

    driver.find_element(By.XPATH, login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_page.header)))

    assert driver.current_url == authorization_page.url

    driver.quit()

def test_login_with_valid_data(authorization_page, main_page, existing_user):

    driver = webdriver.Chrome()
    driver.get(authorization_page.url)

    driver.find_element(By.XPATH, authorization_page.email_input).send_keys(existing_user.email)
    driver.find_element(By.XPATH, authorization_page.password_input).send_keys(existing_user.password)

    driver.find_element(By.XPATH, authorization_page.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.header)))

    assert driver.current_url == main_page.url

    driver.quit()

@pytest.mark.parametrize('email',['non_exiting@user.com','ek_bar_19_111@test.com'])
def test_attempt_to_login_with_invalid_data(authorization_page, main_page, email):

    driver = webdriver.Chrome()
    driver.get(authorization_page.url)

    driver.find_element(By.XPATH, authorization_page.email_input).send_keys("non_exiting@user.com")
    driver.find_element(By.XPATH, authorization_page.password_input).send_keys(password_generator())

    driver.find_element(By.XPATH, authorization_page.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_page.header)))

    assert driver.current_url == authorization_page.url

    driver.quit()

def test_logout(authorization_page, main_page, profile_page, existing_user):

    driver = webdriver.Chrome()

    login(driver,existing_user)

    driver.find_element(By.XPATH, sticky_bar_open_profile_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, profile_page.header)))

    driver.find_element(By.XPATH, profile_page.exit_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_page.header)))
    assert driver.current_url == authorization_page.url

    driver.quit()
