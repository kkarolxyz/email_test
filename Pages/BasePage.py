from selenium import webdriver
from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from Data.TestData import TestData


class BasePage():
    def __init__(self, drier):
        self.driver = drier


class HomePage(BasePage):
    def __init__(self, drier):
        super().__init__(drier)
        self.driver.get(TestData.base_url)
    def is_title_matches(self):
        return TestData.title_homePage in self.driver.title