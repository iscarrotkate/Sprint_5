from selenium.webdriver.common.by import By

from tools.locators import constructor_fillings, constructor_sauces, constructor_bread
from tools.urls import main_page_url

class TestConstructor:

    def test_navigation_to_sauces(self, driver):

        driver.get(main_page_url)

        driver.find_element(By.XPATH, constructor_sauces).click()

        assert 'current' in driver.find_element(By.XPATH, constructor_sauces).get_attribute("class")

    def test_navigation_to_fillings(self, driver):

        driver.get(main_page_url)

        driver.find_element(By.XPATH, constructor_fillings).click()

        assert 'current' in driver.find_element(By.XPATH, constructor_fillings).get_attribute("class")


    def test_navigate_back_to_default_section(self, driver):

        driver.get(main_page_url)

        driver.find_element(By.XPATH, constructor_sauces).click()
        driver.find_element(By.XPATH, constructor_bread).click()

        assert 'current' in driver.find_element(By.XPATH, constructor_bread).get_attribute("class")
