#!/usr/bin/python
"""
.. module:: get_webdriver

This return same webdriver instance for all testcases run as testsuites

"""
'''import statement'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from utils import gui_constants as const

def get_driver(driver_name):
    driver_name = driver_name.lower()
    if driver_name == 'chrome':
        chrome_options = Chrome_Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(executable_path=const.driver_location,options=chrome_options)
        driver.maximize_window()
    elif driver_name == 'firefox':
        firefox_options = Firefox_Options()
        driver = webdriver.Firefox(options=firefox_options)
    elif driver_name == 'safari':
        driver = webdriver.Safari()
    else:
        raise EnvironmentError("""Driver name did not match allowed options.
            Allowed Options: ["chrome", "firefox", "safari"]
            """.format(driver_name))
    return driver