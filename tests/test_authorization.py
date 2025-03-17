from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from tools.helpers import login
from tools.locators import *
from tools.urls import *
from tools.helpers import password_generator
from tools.urls import main_page_url, registration_page_url, password_recovery_page_url

class TestAuthorization:

    @pytest.mark.parametrize(
        'page, login_button',
        [
            [main_page_url, sticky_bar_open_profile_button],
            [main_page_url, main_enter_to_account_button],
            [registration_page_url, registration_login_button],
            [password_recovery_page_url, recovery_login_button]
        ]
    )
    def test_open_login_form_by_unauthorized_user(self, driver, page, login_button):

        driver.get(page)

        driver.find_element(By.XPATH, login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_header)))

        assert driver.current_url == authorization_page_url

    def test_login_with_valid_data(self, driver, existing_user):

        driver.get(authorization_page_url)

        driver.find_element(By.XPATH, authorization_email_input).send_keys(existing_user['email'])
        driver.find_element(By.XPATH, authorization_password_input).send_keys(existing_user['password'])

        driver.find_element(By.XPATH, authorization_login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_header)))

        assert driver.current_url == main_page_url

    @pytest.mark.parametrize('email',['non_exiting@user.com','ek_bar_19_111@test.com'])
    def test_attempt_to_login_with_invalid_data(self, driver, email):

        driver.get(authorization_page_url)

        driver.find_element(By.XPATH, authorization_email_input).send_keys(email)
        driver.find_element(By.XPATH, authorization_password_input).send_keys(password_generator())

        driver.find_element(By.XPATH, authorization_login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_header)))

        assert driver.current_url == authorization_page_url

    def test_logout(self, driver, existing_user):

        login(driver,existing_user)

        driver.find_element(By.XPATH, sticky_bar_open_profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, profile_header)))

        driver.find_element(By.XPATH, profile_exit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_header)))
        assert driver.current_url == authorization_page_url
