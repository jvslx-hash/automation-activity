from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
from pages_web.my_account_page import MyAccountPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field_class = (By.NAME, "email")
        self.send_email_button = (By.XPATH, "//button[@type='submit' and normalize-space()='Enviar']")
        self.send_token_button = (By.XPATH, "//button[normalize-space()='Confirmar']")
        self.token_field = (By.NAME, "token") 
        self.button_my_account = (By.CLASS_NAME, "ButtonLogin_Container__sgzuk")
        self.button_entrar_com_email_e_senha = (By.XPATH, "//div[normalize-space()='Entrar com email e senha']")
        self.email_field_enter_with_email_and_password = (By.XPATH, "//input[@placeholder='ex.: exemplo@mail.com']")
        self.password_field_enter_with_email_and_password = (By.XPATH, "//input[@type='password']")
        self.sign_in_button = (By.XPATH, "//button[@type='submit' and normalize-space()='Entrar']")
        self.message_user_or_password_incorrect = (By.XPATH, "//div[@role='alert' and normalize-space()='Usuário e/ou senha incorretos']")


    def fill_email_field(self, email_capturado):
        self.send_keys_to_element(*self.email_field_class, email_capturado)
        #self.send_keys_to_element(*self.email_field_class, Keys.ENTER)
        time.sleep(4)

    def click_send_email(self):
        send_email_button = self.find_element(*self.send_email_button)
        self.driver.execute_script("arguments[0].click();", send_email_button)
        time.sleep(2)

    def fill_token_field(self, code_text):
        self.send_keys_to_element(*self.token_field, code_text)
        time.sleep(1)

    def click_send_token(self):
        self.wait_for_element_to_be_clickable(*self.send_token_button)
        time.sleep(4)

    def email_message(self):
        return self.find_element(*self.button_my_account).text
    
    def click_my_account(self):
        self.wait_for_element_to_be_clickable(*self.button_my_account)
        time.sleep(2)
        return MyAccountPage(self.driver)
    
    # EMAIL E SENHA

    def click_entrar_com_email_e_senha(self):
        self.scroll_to_element(*self.button_entrar_com_email_e_senha)
        self.wait_for_element_to_be_clickable(*self.button_entrar_com_email_e_senha)
        time.sleep(1)

    def fill_login_field(self, data):
        self.send_keys_to_element(*self.email_field_enter_with_email_and_password, data["email"])

    def fill_password_field(self, data):
        self.send_keys_to_element(*self.password_field_enter_with_email_and_password, data["password"])
        time.sleep(1)

    def click_sign_in_button(self):
        self.wait_for_element_to_be_clickable(*self.sign_in_button)    
        time.sleep(4)

    def validate_message_user_or_password_incorrect(self):
        assert self.is_element_displayed(*self.message_user_or_password_incorrect)    







    
        






     