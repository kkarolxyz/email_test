from selenium.webdriver.common.by import By
class Locators():

    #permission to process personal data
    personal_data = (By.XPATH, "//*[@id='pageMainContainer']/div[8]/div[1]/div[2]/div/div[6]/button[2]")

    #e-mail page icon
    email_page = (By.CLASS_NAME, "mail")