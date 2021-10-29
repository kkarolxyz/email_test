import unittest
from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from selenium import webdriver
from Data.TestData import TestData
from Pages.BasePage import HomePage

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
        assert self.homePage.is_title_matches()

if __name__ == '__main__':
    unittest.main()