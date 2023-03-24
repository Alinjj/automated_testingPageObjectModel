import time
import names
from .base_page import BasePage
from .locators import *

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.driver.current_url, 'not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form not found'


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.CHECK_IN_FORM), 'login form not found'

    def register_new_user(self):
        self.driver.find_element(*CheckInPageLocators.LOGIN_CHECK_IN).send_keys(str(names.get_last_name()) + "@fakemail.org")
        password = (str(time.time()) + str(names.get_first_name(gender='female')))
        self.driver.find_element(*CheckInPageLocators.LOGIN_CHECK_IN_PSWRD).send_keys(password)
        self.driver.find_element(*CheckInPageLocators.LOGIN_CHECK_IN_PSWRD_CONFIRM).send_keys(password)
        self.driver.find_element(*CheckInPageLocators.LOGIN_CHECK_IN_SUBMIT).click()

