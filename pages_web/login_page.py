from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
from pages_web.my_account_page import MyAccountPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field_class = (By.NAME, "email")
        self.send_email_button = (By.XPATH, "//div[contains(@class, 'vtex-login-2-x-sendButton')]/button")
        self.send_token_button = (By.XPATH, "//button[normalize-space()='Confirmar']")
        self.token_field = (By.NAME, "token") 
        self.button_my_account = (By.CLASS_NAME, "ButtonLogin_Container__sgzuk")


    def fill_email_field(self, email_capturado):
        self.send_keys_to_element(*self.email_field_class, email_capturado)
        self.send_keys_to_element(*self.email_field_class, Keys.ENTER)
        time.sleep(4)

    # def click_send_email(self):
    #     self.wait_for_element_to_be_clickable(*self.send_email_button)
    #     time.sleep(2)

    def fill_token_field(self, code_text):
        self.send_keys_to_element(*self.token_field, code_text)
        time.sleep(1)

    def click_send_token(self):
        self.wait_for_element_to_be_clickable(*self.send_token_button)
        time.sleep(2)

    def email_message(self):
        return self.find_element(*self.button_my_account).text
    
    def click_my_account(self):
        self.wait_for_element_to_be_clickable(*self.button_my_account)
        time.sleep(2)
        return MyAccountPage(self.driver)

    
        






     