from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_on_my_account = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div/section/main/main/div[1]/div/div/article/main/div[1]/div[2]/div")
        self.authentication_button = (By.XPATH, "//a[@href='#/authentication']")
        self.define_password_button = (By.XPATH, "//button[normalize-space()='Definir senha']")
        self.token_password_field = (By.XPATH, "//input[@type='text' and contains(@class, 'vtex-styleguide-9-x-input')]")
        self.new_password_field = (By.XPATH, "//input[@type='password']")
        self.save_password_button = (By.XPATH, "//button[.//div[normalize-space(text())='Salvar senha']]")
        self.save_password_button_disabled = (By.XPATH, "//button[normalize-space()='Salvar senha' and (@disabled or @aria-disabled='true')]")
        self.masked_password_text = (By.XPATH, "//div[text()='******************']")

    def validate_email_on_my_account(self):
        return self.find_element(*self.email_on_my_account).text  

    def click_authentication_button(self):
        self.wait_for_element_to_be_clickable(*self.authentication_button)
        time.sleep(1)

    def click_define_password_button(self):
        self.wait_for_element_to_be_clickable(*self.define_password_button)
        time.sleep(1)

    def fill_token_password_field(self, code_password_text):
        self.send_keys_to_element(*self.token_password_field, code_password_text) 

    # def get_save_button_disabled_status(self):
    #     try:
    #         save_button = self.find_element(*self.save_password_button)
    #         aria_disabled = save_button.get_attribute("aria-disabled")
    #         regular_disabled = save_button.get_attribute("disabled")
    #         return (aria_disabled == "true") or (regular_disabled is not None)
            
    #     except Exception:
    #         return False     

    def fill_form_password_with_less_than_eight_characters(self, data):
        self.send_keys_to_element(*self.new_password_field, data["password"])
        time.sleep(2)
        assert self.is_element_displayed(*self.save_password_button_disabled)
        
        element = self.find_element(*self.new_password_field)
        element.click()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def fill_form_password_without_numbers(self, data):
        self.send_keys_to_element(*self.new_password_field, data["password"])
        time.sleep(2)
        assert self.is_element_displayed(*self.save_password_button_disabled)

        element = self.find_element(*self.new_password_field)
        element.click()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def fill_form_password_without_lowercase(self, data):
        self.send_keys_to_element(*self.new_password_field, data["password"])
        time.sleep(2)
        assert self.is_element_displayed(*self.save_password_button_disabled)

        element = self.find_element(*self.new_password_field)
        element.click()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def fill_form_password_without_uppercase(self, data):
        self.send_keys_to_element(*self.new_password_field, data["password"])
        time.sleep(2)
        assert self.is_element_displayed(*self.save_password_button_disabled)   

        element = self.find_element(*self.new_password_field)
        element.click()
        element.send_keys(Keys.COMMAND + "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def fill_form_correct_password(self,data):
        self.send_keys_to_element(*self.new_password_field, data["password"])
        time.sleep(2)

    def click_save_password(self):    
        self.wait_for_element_to_be_clickable(*self.save_password_button) 
        time.sleep(2)

    def validate_masked_password(self):
        assert self.is_element_displayed(*self.masked_password_text)   