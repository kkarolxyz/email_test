from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

class TestData():

    chrome_driver_path = "./chromedriver.exe"
    base_url = "https://www.onet.pl"
    title_homePage = "Onet"
    title_email_page = "Poczta"
    valid_email_name = "pythonselenium@onet.pl"
    valid_pass = "Python1234!"
    invalid_pass = "XYZ"
    