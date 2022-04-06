#!/usr/bin/python
"""
.. module:: utility

Utilities to be used across pages.
"""

'''import statements'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import POLL_FREQUENCY
from utils import gui_constants as const

class Utility():
    '''
    Class contains function that support various common functions requires in test.
    '''
    def wait_and_find_element(self, driver, selectorName, selectorVal):
        '''
        Wait for element to be visible and then return element.

        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS, BY.ID or BY.XPATH
        :param selectorVal: ID, CSS or XAPTH of the element.

        :return: Returns only one element
        '''

        WebDriverWait(driver, const.refresh_tout).until(EC.visibility_of_element_located((selectorName, selectorVal)))
        return driver.find_element(selectorName, selectorVal)


    def wait_and_find_elements(self, driver, selectorName, selectorVal):
        '''
        Wait for all elements to be visible.

        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS, BY.ID or BY.XPATH
        :param selectorVal: ID, CSS or XAPTH of the element.

        :return: Returns list of element.
        '''
        WebDriverWait(driver, const.refresh_tout).until(EC.visibility_of_all_elements_located((selectorName, selectorVal)))
        return driver.find_elements(selectorName, selectorVal)


    def wait_for_element_invisibility(self, driver, selectorName, selectorVal):
        '''
        Wait for element to be invisible.
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS, BY.ID or BY.XPATH
        :param selectorVal: ID, CSS or XAPTH of the element.
        '''
        WebDriverWait(driver, const.refresh_tout).until(EC.invisibility_of_element_located((selectorName, selectorVal)))


    def click(self, driver, selectorName, selectorVal):
        '''
        Wait for element to be visible and then click on that element
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        :return:
        '''

        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        element.click()


    def enter_text(self, driver, selectorName, selectorVal, text):
        '''
        Wait for element to be visible and then enter text in that element.
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        :param text: text to be entered.
        :return:
        '''

        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        element.send_keys(text)


    def find_element_text(self, driver, selectorName, selectorVal):
        '''
        Wait for Element to be visible and then returns text of that element.
        :param driver: webDriver reference variable
        :param selectorName: selector parameters like BY.CSS or BY.XPATH
        :param selectorVal: CSS or XAPTH of the element.
        '''

        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        return element.text

    def have_element_displayed(self, driver, selectorName, selectorVal):
        '''
            Wait for Element to be visible
            :param driver: webDriver reference variable
            :param selectorName: selector parameters like BY.CSS or BY.XPATH
            :param selectorVal: CSS or XAPTH of the element.
        '''
        WebDriverWait(driver, const.refresh_tout, poll_frequency=POLL_FREQUENCY).until(EC.visibility_of_element_located((selectorName, selectorVal)))

    def switch_to_frame(self, driver, frame_id):
        WebDriverWait(driver, const.refresh_tout).until(EC.frame_to_be_available_and_switch_to_it(frame_id))
