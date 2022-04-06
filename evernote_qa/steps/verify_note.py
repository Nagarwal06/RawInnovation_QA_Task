#!/usr/bin/python
"""
.. module:: verify_note

Login to web application using the valid credentials and verify the created note title.
And then open the created note.
"""

'''import statement'''
from pages.login_page import LoginPage
from pages.verify_page import VerifyPage
from pages.home_page import HomePage
from pages.get_webdriver import get_driver
from utils import gui_constants as const
from behave import *
import time

'''Object variables'''
login_obj = LoginPage()
verify_obj = VerifyPage()
home_obj = HomePage()

@Given('User is on signin page to verify')
def navigate_to_login_page(context):
    global driver
    driver = get_driver(const.browser_name)
    login_obj.navigate_to_login_page(driver)

@When('User enter email address and clicks continue to verify')
def enter_username(context):
    login_obj.enter_username(driver, const.username)
    login_obj.click_continue_btn(driver)

@When('User enter password and click signin to verify')
def enter_password(context):
    login_obj.enter_password(driver, const.password)
    login_obj.click_continue_btn(driver)
    time.sleep(45)

@When('click on the created note')
def click_on_created_note(context):
    verify_obj.click_created_note(driver)

@Then('User verify the note')
def create_a_new_note(context):
    time.sleep(10)
    note_title_text = verify_obj.verify_note(driver)
    assert note_title_text == const.note_title
    driver.close()
    driver.quit()
