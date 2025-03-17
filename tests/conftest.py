from selenium import webdriver
import pytest

@pytest.fixture
def existing_user():

    return {
        'name': 'carrot_kate_123',
        'email': 'ek_bar_19_111@test.com',
        'password': 'qwerty'
    }

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()