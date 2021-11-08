import time
from selenium import webdriver
from selenium.webdriver.common import by
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
       WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by_locator))).click()

    def is_element_located(self, by_locator):
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator))
    
    def enter_text(self,by_locator, send_text):
        WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(by_locator)).send_keys(send_text)

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
    
    def submit_button(self):
        try : 
            self.click(Locators.submit_button)
        except Exception as error:
            print(error,"Submit button is not visible")

class MailPageLoginValid(BasePage):
    def __init__(self, drier):
        super().__init__(drier)
    
    def is_email_form_located(self):
        try:
            self.is_element_located(Locators.email_form)
        except Exception as error:
            print(error,"E-Mail form is not visible")

    def login_remember_false(self):
        self.click(Locators.login_remember)

    def insert_valid_email_name(self):
        self.driver.find_element(*Locators.email_form).clear()
        self.enter_text(Locators.email_form, TestData.valid_email_name)
        
    def insert_valid_pass(self):
        try:
            self.driver.find_element(*Locators.password_form).clear()
            self.enter_text(Locators.password_form,TestData.valid_pass)
        except Exception as error:
            print(error,"Fill password - FAILED")
    
    def is_user_mail_page_available(self):
        try:
            self.is_element_located(Locators.user_page_available)
        except Exception as error:
            print(error, "User email page not available")

class MailPageLoginInValid(BasePage):

    def __init__(self, drier):
        super().__init__(drier)
    
    def insert_invalid_pass(self):
        try:
            self.driver.find_element(*Locators.password_form).clear()
            self.enter_text(Locators.password_form, TestData.invalid_pass)
        except Exception as error:
            print(error, "Fill invalid password - FAILED")
    
    
    
