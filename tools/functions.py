from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tools.pages import RegistrationPage, AuthorizationPage, MainPage

def login_generator():

    return 'ekaterina_baranova_19_' + str(randint(100, 999)) + '@email.com'

def password_generator():

    return randint(100000, 999999)

def fill_in_registration_form(driver, name, email, password):
    registration_page = RegistrationPage()
    driver.get(registration_page.url)

    driver.find_element(By.XPATH, registration_page.name_input).send_keys(name)
    driver.find_element(By.XPATH, registration_page.email_input).send_keys(email)
    driver.find_element(By.XPATH, registration_page.password_input).send_keys(password)

def login(driver, existing_user):

    authorization_page = AuthorizationPage()
    main_page = MainPage()

    if driver.current_url == 'data:,':
        initial_url = main_page.url
    else:
        initial_url = driver.current_url

    driver.get(authorization_page.url)

    driver.find_element(By.XPATH, authorization_page.email_input).send_keys(existing_user.email)
    driver.find_element(By.XPATH, authorization_page.password_input).send_keys(existing_user.password)

    driver.find_element(By.XPATH, authorization_page.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.header)))

    driver.get(initial_url)
