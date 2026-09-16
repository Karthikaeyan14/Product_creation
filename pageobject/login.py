from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Login:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,40)
        self.sign_button=(By.LINK_TEXT,"Sign in")
        self.email=(By.ID,'login')
        self.password=(By.ID,"password")
        self.login_button=(By.XPATH,"//button[text()='Log in']")
        self.error_message=(By.XPATH,"//div[@class='alert alert-danger']")
    
    def signup(self):
        self.wait.until(EC.element_to_be_clickable(
            self.sign_button
        )).click()
    
    def login_details(self, username, password):

     email = self.wait.until(
        EC.visibility_of_element_located(self.email)
    )
     email.clear()
     email.send_keys(username)
 
     password_field = self.wait.until(
        EC.visibility_of_element_located(self.password)
     )
     password_field.clear()
     password_field.send_keys(password)

     self.wait.until(
        EC.element_to_be_clickable(self.login_button)).click()
     
     def warning_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text