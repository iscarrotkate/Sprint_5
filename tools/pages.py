from tools.locators import *


class MainPage:

    def __init__(self):
        self.url = 'https://stellarburgers.nomoreparties.site/'
        self.header = main_header
        self.account_button = sticky_bar_open_profile_button
        self.enter_to_account_button = main_enter_to_account_button

class RegistrationPage:

    def __init__(self):
        self.url = 'https://stellarburgers.nomoreparties.site/register'
        self.header = registration_header
        self.name_input = registration_name_input
        self.email_input = registration_email_input
        self.password_input = registration_password_input
        self.register_button = registration_register_button
        self.password_error = registration_invalid_password_error
        self.login_button = registration_login_button

class AuthorizationPage:

    def __init__(self):
        self.url = 'https://stellarburgers.nomoreparties.site/login'
        self.header = authorization_header
        self.email_input = authorization_email_input
        self.password_input = authorization_password_input
        self.login_button = authorization_login_button

class PasswordRecoveryPage:

    def __init__(self):
        self.url = 'https://stellarburgers.nomoreparties.site/forgot-password'
        self.header = recovery_header
        self.email_input = recovery_email_input
        self.recover_button = recovery_recover_button
        self.login_button = recovery_login_button

class ProfilePage:

    def __init__(self):
        self.url = 'https://stellarburgers.nomoreparties.site/account/profile'
        self.header =profile_header
        self.exit_button=profile_exit_button
