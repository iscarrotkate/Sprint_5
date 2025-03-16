from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from tools.functions import login_generator, password_generator, fill_in_registration_form


def test_registration_new_user_valid_data(registration_page, authorization_page):

    driver = webdriver.Chrome()
    driver.get(registration_page.url)

    email = login_generator()
    name = email.split('@')[0]

    fill_in_registration_form(driver, name, email, password_generator())

    driver.find_element(By.XPATH, registration_page.register_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_page.header)))

    assert driver.current_url == authorization_page.url

    driver.quit()

def test_registration_new_user_with_empty_name(registration_page):

    driver = webdriver.Chrome()
    driver.get(registration_page.url)

    fill_in_registration_form(driver, "", login_generator(), password_generator())

    driver.find_element(By.XPATH, registration_page.register_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_page.header)))

    assert driver.current_url == registration_page.url

    driver.quit()

@pytest.mark.parametrize('email',['email','email@, email@first','@first.second', 'first.second'])
def test_registration_email_format_validation(registration_page, email):

    driver = webdriver.Chrome()
    driver.get(registration_page.url)

    fill_in_registration_form(driver, login_generator().split('@')[0], email, password_generator())

    driver.find_element(By.XPATH, registration_page.register_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_page.header)))

    assert driver.current_url == registration_page.url

    driver.quit()

def test_registration_invalid_password_returns_error(registration_page):

    driver = webdriver.Chrome()
    driver.get(registration_page.url)

    email = login_generator()
    name = email.split('@')[0]

    fill_in_registration_form(driver, name, email, '12345')

    driver.find_element(By.XPATH, registration_page.register_button).click()

    assert driver.find_element(By.XPATH, registration_page.password_error).is_displayed()

    driver.quit()
