from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time

class AccountPage(BasePage):
    class Locators:
        enter_with_email_button = (AppiumBy.XPATH, "//android.view.View[@resource-id='Entrar com e-mail']")
        confirm_enter_with_email_button = (AppiumBy.ACCESSIBILITY_ID, "Entrar com e-mail e senha")
        email_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='E-mail']")
        password_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='Senha']")
        login_button = (AppiumBy.XPATH, "//android.view.View[@resource-id='Entrar']")
        change_password_button = (AppiumBy.ACCESSIBILITY_ID, "Alterar\nsenha")
        alert_invalid_password = (AppiumBy.ACCESSIBILITY_ID, "Insira uma senha válida")
        alert_wrong_password = (AppiumBy.XPATH, "(//android.view.View[@content-desc='Usuário ou senha inválidos.'])[1]")
        

    def __init__(self, driver):
        super().__init__(driver)

    def click_enter_with_email_button(self):
        self.click_element(*self.Locators.enter_with_email_button) 
        time.sleep(0.5)

    def click_confirm_enter_with_email_button(self):
        self.click_element(*self.Locators.confirm_enter_with_email_button) 
        time.sleep(0.5)

    def input_email(self, data):
        self.click_element(*self.Locators.email_field) 
        self.send_keys_to_element(*self.Locators.email_field, data["email"])    

    def input_password(self, data):
        self.click_element(*self.Locators.password_field) 
        self.send_keys_to_element(*self.Locators.password_field, data["password"]) 

    def click_login_button(self):
        self.click_element(*self.Locators.login_button) 
        time.sleep(5)     

    def validate_change_password_button_is_displayed(self):
       assert self.is_element_displayed(*self.Locators.change_password_button)

    def validate_alert_invalid_password_displayed(self):
       assert self.is_element_displayed(*self.Locators.alert_invalid_password) 

    def validate_alert_wrong_password_displayed(self):
        assert self.is_element_displayed(*self.Locators.alert_wrong_password) 


        

