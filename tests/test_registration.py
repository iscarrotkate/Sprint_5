from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from tools.helpers import login_generator, password_generator, fill_in_registration_form
from tools.locators import registration_register_button, authorization_header, registration_header, \
    registration_invalid_password_error
from tools.urls import registration_page_url, authorization_page_url

class TestRegistration:

    def test_registration_new_user_valid_data(self, driver):

        driver.get(registration_page_url)

        email = login_generator()
        name = email.split('@')[0]

        fill_in_registration_form(driver, name, email, password_generator())

        driver.find_element(By.XPATH, registration_register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_header)))

        assert driver.current_url == authorization_page_url

    def test_registration_new_user_with_empty_name(self, driver):

        driver.get(registration_page_url)

        fill_in_registration_form(driver, "", login_generator(), password_generator())

        driver.find_element(By.XPATH, registration_register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_header)))

        assert driver.current_url == registration_page_url

    @pytest.mark.parametrize('email',['email','email@, email@first','@first.second', 'first.second'])
    def test_registration_email_format_validation(self, driver, email):

        driver.get(registration_page_url)

        fill_in_registration_form(driver, login_generator().split('@')[0], email, password_generator())

        driver.find_element(By.XPATH, registration_register_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_header)))

        assert driver.current_url == registration_page_url

    def test_registration_invalid_password_returns_error(self, driver):

        driver.get(registration_page_url)

        email = login_generator()
        name = email.split('@')[0]

        fill_in_registration_form(driver, name, email, '12345')

        driver.find_element(By.XPATH, registration_register_button).click()

        assert driver.find_element(By.XPATH, registration_invalid_password_error).is_displayed()
