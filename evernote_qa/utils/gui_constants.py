browser_name = "chrome"
driver_location = r'C:\Program Files\Python37\chromedriver.exe'

login_url = r"https://www.evernote.com/Login.action"
username = 'nitishatest666@gmail.com'
password = 'Test@123'

refresh_tout = 10

#Login page constants
username_textfeild = 'username'
login_btn = 'loginButton'
password_textfeild = 'password'
login_alert_xpath = "//div[contains(text(),'Incorrect password. You modified your password')]"
password_err_msg = "Incorrect password"
logged_in_xpath = "//div[@id='qa-HOME']"
#home page constants
note_xpath = "//span[contains(text(),'Notes')]"
create_note_xpath = "//button[@id='qa-NAVBAR_NOTE_ADD_BUTTON']"
iframe_id = 'qa-COMMON_EDITOR_IFRAME'
note_title_xpath = "//en-noteheader/div[1]/div[2]/textarea[1]"
note_description_xpath = "//en-note[@id='en-note']"
note_title = "Test_for_evernote_111111"
note_description = "Creatad a note to test the note functionality"
account_menu = "//div[@id='qa-NAV_USER']/div[1]"
logout_btn_id = "qa-ACCOUNT_DROPDOWN_LOGOUT"
exit_btn_id = "qa-LOGOUT_CONFIRM_DIALOG_SUBMIT"

#verify note page constants
title_xpath = "//en-noteheader/div[1]/div[2]/textarea[1]"
home_menu_xpth = "//span[contains(text(),'Home')]"