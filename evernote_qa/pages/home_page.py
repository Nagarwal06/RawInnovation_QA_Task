#!/usr/bin/python
"""
.. module:: home_page

It contains Home Page functionalities.
"""

'''import statement'''
from selenium.webdriver.common.by import By
from utils import gui_constants as const
from utils.utility import Utility
import time
from selenium.webdriver.common.action_chains import ActionChains

utility_obj = Utility()


class HomePage(object):
    '''
        Class contains Home/Create Note Page functionalities
        '''

    def cretae_note(self, driver):
        #Cretae a new Note
        actions = ActionChains(driver)
        note_button = driver.find_element_by_xpath(const.note_xpath)
        add_button = driver.find_element_by_xpath(const.create_note_xpath)
        actions.move_to_element(note_button)
        actions.click(add_button)
        actions.perform()

    def switch_iframe(self, driver, frame_id):
        # Switch to iframe
        time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    def add_note_title(self, driver, note_title):
        #add note title.
        utility_obj.enter_text(driver, By.XPATH, const.note_title_xpath, note_title)

    def add_note_description(self, driver, note_description):
        #Add note description
        utility_obj.enter_text(driver, By.XPATH, const.note_description_xpath, note_description)

    def switch_to_main_content(self, driver):
        #Switch back to the main HTML
        driver.switch_to.default_content()

    def account_menu(self, driver):
        #Click on the account menu
        utility_obj.click(driver, By.XPATH, const.account_menu)

    def logout(self, driver):
        #Click on the logout button
        utility_obj.click(driver, By.ID, const.logout_btn_id)

    def click_exit_btn(self, driver):
        #Click on the exit button to logout successfully
        utility_obj.click(driver, By.ID, const.exit_btn_id)