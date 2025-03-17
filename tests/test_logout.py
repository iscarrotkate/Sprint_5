from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tools.helpers import login
from tools.locators import sticky_bar_open_profile_button, profile_exit_button, profile_header, authorization_header
from tools.urls import authorization_page_url


class TestLogout:
    def test_logout(self, driver, existing_user):

        login(driver, existing_user)

        driver.find_element(By.XPATH, sticky_bar_open_profile_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, profile_header)))

        driver.find_element(By.XPATH, profile_exit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, authorization_header)))
        assert driver.current_url == authorization_page_url
