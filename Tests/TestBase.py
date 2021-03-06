import unittest
import time

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from selenium import webdriver
from Data.TestData import TestData
from Pages.BasePage import HomePage, MailPage, MailPageLoginValid, MailPageLoginInValid

class TestPageBase(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.chrome_driver_path)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class TestPage(TestPageBase):
    def setUp(self):
        super().setUp()

    def test_A_home_page_loaded_succesfully(self):
        self.homePage = HomePage(self.driver)
        self.homePage.permission_is_true()
        try:
            assert self.homePage.is_title_matches()
        except Exception as error:
            print(error,"WebPage Failed to load")

    def test_B_mail_page_loaded_succesfully(self):
        self.homePage = HomePage(self.driver)
        self.homePage.permission_is_true()
        self.emailPage = MailPage(self.driver)
        self.emailPage.move_to_email_page()
        assert self.emailPage.is_email_page_loaded()
    

    def test_C_mail_page_login_succesfully(self):
        self.homePage = HomePage(self.driver)
        self.homePage.permission_is_true()
        self.emailPage = MailPage(self.driver)
        self.emailPage.move_to_email_page()
        self.mailPageLogin = MailPageLoginValid(self.driver)
        self.mailPageLogin.is_email_form_located()
        self.mailPageLogin.insert_valid_email_name()
        self.mailPageLogin.insert_valid_pass()
        self.mailPageLogin.login_remember_false()
        self.emailPage.submit_button()
        self.mailPageLogin.is_user_mail_page_available()
        
    def test_D_mail_page_login_unsuccesfully(self):
        self.homePage = HomePage(self.driver)
        self.homePage.permission_is_true()
        self.emailPage = MailPage(self.driver)
        self.emailPage.move_to_email_page()
        self.mailPageLogin = MailPageLoginValid(self.driver)
        self.mailPageLogin.is_email_form_located()
        self.mailPageLogin.insert_valid_email_name()
        self.mailPageInvalid = MailPageLoginInValid(self.driver)
        self.mailPageInvalid.insert_invalid_pass()
        self.mailPageLogin.login_remember_false()
        self.emailPage.submit_button()
        self.driver.execute_script("window.history.go(-1)")
        self.mailPageInvalid.insert_invalid_email()
        self.mailPageLogin.insert_valid_pass()
        self.mailPageLogin.login_remember_false()
        self.emailPage.submit_button()
        self.driver.execute_script("window.history.go(-1)")


if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='results'))
