#!/usr/bin/python
"""
.. module:: valid_login

Login to web application using valid email address and password.
And then click on the login button and verify if the user is logged-in successfully or not.
"""

'''import statement'''
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.get_webdriver import get_driver
from utils import gui_constants as const
from behave import *
import time

'''Object variables'''
login_obj = LoginPage()
home_obj = HomePage()

@Given('Navigate to login page.')
def navigate_to_login_page(context):
    global driver
    driver = get_driver(const.browser_name)
    login_obj.navigate_to_login_page(driver)

@When('We enter valid email and password')
def enter_username_password(context):
    login_obj.enter_username(driver, const.username)
    login_obj.click_continue_btn(driver)
    login_obj.enter_password(driver, const.password)

@Then('click on continue button')
def click_continue(context):
    login_obj.click_continue_btn(driver)

@Then('verify user is logged-in.')
def click_continue(context):
    time.sleep(45)
    login_obj.is_loaded(driver)
    driver.close()
    driver.quit()
