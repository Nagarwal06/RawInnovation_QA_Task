#!/usr/bin/python
"""
.. module:: invalid_login

Login to web application using the valid email address but invalid password.
And then verify the error message.
"""

'''import statement'''
from pages.login_page import LoginPage
from pages.get_webdriver import get_driver
from utils import gui_constants as const
import random
import string
import time
from behave import *

'''Object variables'''
login_obj = LoginPage()

@Given('Navigate to login page')
def navigate_to_login_page(context):
    global driver
    driver = get_driver(const.browser_name)
    login_obj.navigate_to_login_page(driver)

@When('We enter valid email and click continue')
def enter_username(context):
    login_obj.enter_username(driver, const.username)
    login_obj.click_continue_btn(driver)

@When('We enter invalid password and click continue')
def enter_password(context):
    random_pass = ''.join(random.choice(string.digits) for x in range(8))
    login_obj.enter_password(driver, random_pass)
    login_obj.click_continue_btn(driver)
    time.sleep(5)

@Then('Error message should be displayed.')
def verify_error_message(context):
    wrong_password_alert = login_obj.login_alert_text(driver)
    assert const.password_err_msg in wrong_password_alert
    driver.close()
    driver.quit()