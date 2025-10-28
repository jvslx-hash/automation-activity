from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class EmailPage(BasePage):
    def __init__(self, driver, handle_da_americanas):
        super().__init__(driver)
        self.americanas_handle = handle_da_americanas
        self.email_generator_url = "https://temp-mail.io/en"
        self.copy_email_button = (By.XPATH, "//*[@id='__nuxt']/div[1]/main/div[3]/button[1]")
        self.email_handle = None
        self.email_address_field = (By.ID, "email")
        self.email_string = None
        self.message_preview = (By.XPATH, "//*[@id='__nuxt']/div[1]/main/div[6]/aside/div/div[2]/div/ul/li")
        self.confirmation_code_label = (By.XPATH, "//p[string-length(text()) = 6 and number(text()) = number(text())]")
        self.message_preview_password = (By.XPATH, "//*[@id='__nuxt']/div[1]/main/div[6]/aside/div/div[2]/div/ul/li[1]")
        self.confirmation_code_label_password = (By.XPATH, "//*[@id='__nuxt']/div[1]/main/div[6]/aside/div/div[2]/article/div[3]/span/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/p")

    def open_temp_mail_in_new_tab(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get(self.email_generator_url)
        time.sleep(5)
        self.email_handle = self.driver.current_window_handle

        
    def get_email_text(self):
        email_element = self.wait_for_visibility_of_element(*self.email_address_field)
        email_string = email_element.get_attribute('value')
        #print(f"{email_string}")
        return email_string
        
    def return_to_americanas(self):
        self.driver.switch_to.window(self.americanas_handle)
        time.sleep(2)

    def return_to_email(self):
        self.driver.switch_to.window(self.email_handle)
        time.sleep(7)

    def click_message(self):
        self.wait_for_element_to_be_clickable(*self.message_preview)
        time.sleep(2)

    def get_confirmation_code(self):
        code_element = self.wait_for_visibility_of_element(*self.confirmation_code_label)
        code_text = code_element.text
        #print(f"Código capturado: {code_element.text}")
        return code_text
    
    def click_message_password(self):
        self.wait_for_element_to_be_clickable(*self.message_preview_password)
        time.sleep(2)

    def get_confirmation_code_password(self):
        code_password_element = self.wait_for_visibility_of_element(*self.confirmation_code_label_password)
        code_password_text = code_password_element.text
        #print(f"Código capturado: {code_password_element.text}")
        return code_password_text    






    