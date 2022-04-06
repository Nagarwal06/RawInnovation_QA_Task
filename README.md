# RawInnovation_QA_Task
This is the test automation framework based on Python, Selenium and BDD framework used to create testcases to log into a specific web page using a gmail account.

**Pre-Requisites:**

- Python 3 Installed (https://www.python.org/downloads/release/python-368/)
- Download Browser WebDriver e.g. For Chrome:- https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/
- Move Browser Driver in directory (C:\Program Files\Python36).
- Open command prompt/terminal in Administrator mode.
- Install Selenium using command -> pip install selenium.
- Install BDD using command --> pip install behave

**Objective**: Create test automation suite to add, create and edit the notes.

**Architecture** 
_utils_: Utility class having common functions to support test execution.
_pages_: It contains the objects of different pages.
_features_: All test suite and test cases which are to be executed for different features.

**Project Structure:** 
   * evernote_qa
       * feature
          * create_note.feature
          * invalid_login.feature
          * valid_login.feature
          * verify_note.feature
       * pages
          * get_webdriver.py
          * home_page.py
          * login_page.py
          * verify_page.py
       * steps
          * create_note.py
          * invalid_login.py
          * valid_login.py
          * verify_note.py
      * utils
          * gui_constants.py
          * utility.py

**Step-by-step guide to run test using cmd:**
1. Make sure all necessary packages are installed.
2. Either place the driver at location "C:\Program Files\Python36" or update gui_constants.py variable "driver_location" with correct driver location.
3. Open cmd prompt in administrator mode.
4. Change the directory to project path i.e, evernote_qa -> cd evernote_qa
5. Run the command "behave feature\"
6. Wait for test to complete and see result in command prompt.

**Note:** By default, test will be executed for Chrome Browser. Update variable "browser_name" in gui_constants.py file. Allowed Options: ["chrome", "firefox", "safari"]   

Also, please change the username and password in gui_constants.py file to sign with other accounts in the Web Application using gmail account.
