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
from Pages.BasePage import HomePage, MailPage

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


if __name__ == '__main__':
    unittest.main()