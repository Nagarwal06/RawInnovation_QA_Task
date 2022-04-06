#!/usr/bin/python
"""
.. module:: create_note

Login to web application and then create a new note and update the title and description of the note
Then click on the Account menu to logout from the application
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

@Given('User should be logged-in.')
def navigate_to_login_page(context):
    global driver
    driver = get_driver(const.browser_name)
    login_obj.navigate_to_login_page(driver)
    login_obj.enter_username(driver, const.username)
    login_obj.click_continue_btn(driver)
    login_obj.enter_password(driver, const.password)
    login_obj.click_continue_btn(driver)

@When('User clicks on create note')
def create_a_new_note(context):
    time.sleep(45)
    home_obj.cretae_note(driver)

@When('Add a note Tile and description')
def add_note_title_and_description(context):
    home_obj.switch_iframe(driver, const.iframe_id)
    home_obj.add_note_title(driver, const.note_title)
    home_obj.add_note_description(driver, const.note_description)

@When('Click on Account Menu')
def click_account_menu(context):
    time.sleep(5)
    home_obj.switch_to_main_content(driver)
    home_obj.account_menu(driver)

@Then('Click on Logout button')
def logout(context):
    home_obj.logout(driver)
    time.sleep(5)
    driver.close()
    driver.quit()