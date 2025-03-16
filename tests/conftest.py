import pytest

from tools.pages import *

class User:

    def __init__(self, name = None, email = None, password = None):
        self.name = name
        self.email = email
        self.password = password

@pytest.fixture
def registration_page():
    page = RegistrationPage()

    return page

@pytest.fixture
def authorization_page():
    page = AuthorizationPage()

    return page

@pytest.fixture
def main_page():
    page = MainPage()

    return page

@pytest.fixture
def password_recovery_page():
    page = PasswordRecoveryPage()

    return page

@pytest.fixture
def profile_page():
    page = ProfilePage()

    return page

@pytest.fixture
def existing_user():
    user = User('carrot_kate_123', 'ek_bar_19_111@test.com', 'qwerty')

    return user
