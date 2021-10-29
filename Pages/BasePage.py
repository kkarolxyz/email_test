import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from Data.TestData import TestData
from Locators.Locators import Locators


class BasePage():
    def __init__(self, drier):
        self.driver = drier
    
    def click(self, by_locator):
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by_locator))).click()


class HomePage(BasePage):
    def __init__(self, drier):
        super().__init__(drier)
        self.driver.get(TestData.base_url)

    def permission_is_true(self):
        self.click(Locators.personal_data)

    def is_title_matches(self):
        return TestData.title_homePage in self.driver.title

class MailPage(BasePage):
    def __init__(self, drier):
        super().__init__(drier)

    def move_to_email_page(self):
        self.click(Locators.email_page)

    def is_email_page_loaded(self):
        return TestData.title_email_page in self.driver.title