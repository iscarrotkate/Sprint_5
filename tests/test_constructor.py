from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from tools.locators import constructor_fillings, constructor_sauces, constructor_bread


@pytest.mark.parametrize('constructor_option', [constructor_fillings, constructor_sauces])
def test_navigation_between_constructor_sections(main_page, constructor_option):

    driver = webdriver.Chrome()
    driver.get(main_page.url)

    default_section = driver.find_element(By.XPATH, constructor_bread)
    target_section = driver.find_element(By.XPATH, constructor_option)

    target_section.click()

    assert 'current' in target_section.find_element(By.XPATH,"./parent::*").get_attribute("class")

    default_section.click()

    assert 'current' in default_section.find_element(By.XPATH,"./parent::*").get_attribute("class")

    driver.quit()
