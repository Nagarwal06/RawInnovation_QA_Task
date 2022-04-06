#!/usr/bin/python
"""
.. module:: login_page

It contains Login Page functionalities.
"""

'''import statement'''
from selenium.webdriver.common.by import By
from utils import gui_constants as const
from utils.utility import Utility

utility_obj = Utility()


class LoginPage(object):
    '''
        Class contains Login Page functionalities
        '''

    def navigate_to_login_page(self, driver):
        # Navigate to Login Page
        driver.get(const.login_url)

    def enter_username(self, driver, user):
        # Enter User name.
        utility_obj.enter_text(driver, By.ID, const.username_textfeild, user)

    def click_continue_btn(self, driver):
        # Click on Continue button.
        utility_obj.click(driver, By.ID, const.login_btn)

    def enter_password(self, driver, password):
        # Enter password.
        utility_obj.enter_text(driver, By.ID, const.password_textfeild, password)

    def login_alert_text(self, driver):
        #Verify the error incase of invalid credentials.
        return utility_obj.find_element_text(driver, By.XPATH, const.login_alert_xpath)

    def is_loaded(self, driver):
        return utility_obj.have_element_displayed(driver, By.XPATH, const.logged_in_xpath)