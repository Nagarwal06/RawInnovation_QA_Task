#!/usr/bin/python
"""
.. module:: verify_page

It contains the functionalities of open the created note and verify if the note is creataed or not.
"""

'''import statement'''
from selenium.webdriver.common.by import By
from utils.utility import Utility
from utils import gui_constants as const

utility_obj = Utility()


class VerifyPage(object):
    '''
        Class contains Verify the note functionalities
        '''
    created_note_xpath = "//span[contains(text(),'%s')]" % const.note_title


    def click_created_note(self, driver):
        #Click on the note which is created previously
        utility_obj.click(driver, By.XPATH, self.created_note_xpath)


    def verify_note(self, driver):
        #Verify the title of the created note
        ele_text = driver.execute_script(
            "return document.getElementById('qa-COMMON_EDITOR_IFRAME').contentWindow.document.getElementsByTagName('en-noteheader')[0].querySelector('div').lastChild.lastChild.textContent")
        return ele_text