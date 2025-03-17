from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tools.locators import registration_name_input, registration_email_input, registration_password_input, \
    authorization_email_input, authorization_password_input, authorization_login_button, main_header
from tools.urls import registration_page_url, main_page_url, authorization_page_url


def login_generator():

    return 'ekaterina_baranova_19_' + str(randint(100, 999)) + '@email.com'

def password_generator():

    return randint(100000, 999999)

def fill_in_registration_form(driver, name, email, password):
    driver.get(registration_page_url)

    driver.find_element(By.XPATH, registration_name_input).send_keys(name)
    driver.find_element(By.XPATH, registration_email_input).send_keys(email)
    driver.find_element(By.XPATH, registration_password_input).send_keys(password)

def login(driver, existing_user):

    if driver.current_url == 'data:,':
        initial_url = main_page_url
    else:
        initial_url = driver.current_url

    driver.get(authorization_page_url)

    driver.find_element(By.XPATH, authorization_email_input).send_keys(existing_user['email'])
    driver.find_element(By.XPATH, authorization_password_input).send_keys(existing_user['password'])

    driver.find_element(By.XPATH, authorization_login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_header)))

    driver.get(initial_url)
