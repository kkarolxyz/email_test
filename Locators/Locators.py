from selenium.webdriver.common.by import By
class Locators():

    #permission to process personal data
    personal_data = (By.XPATH, "//*[@id='pageMainContainer']/div[8]/div[1]/div[2]/div/div[6]/button[2]")

    #e-mail page icon
    email_page = (By.CLASS_NAME, "itemMail")

    #e-mail form is visable
    email_form = (By.XPATH, "//*[@id='mailFormLogin']") 

    #password form
    password_form = (By.XPATH, "//*[@id='mailFormPassword']")

    #submit button 
    submit_button = (By.XPATH, "//*[@id='loginForm']/div[3]/input")

    #remember login 
    login_remember = (By.XPATH, "//*[@id='loginForm']/div[3]/label/span[1]")

    #user email page
    user_page_available = (By.XPATH, "//*[@id='wrapper']/div[4]/aside/div[2]/nav")