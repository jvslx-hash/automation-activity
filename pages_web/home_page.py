from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
import time
from pages_web.email_page import EmailPage
from pages_web.login_page import LoginPage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.americanas_url = "https://www.americanas.com.br/"
        self.email_generator_url = "https://temp-mail.io/en"
        self.login_button_class_name = (By.CLASS_NAME, "ButtonLogin_Container__sgzuk")
        self.close_oferta_relampago_button_class = (By.CLASS_NAME, "show-element")
        self.copy_email_button = (By.XPATH, "//*[@id='__nuxt']/div[1]/main/div[3]/button[1]")

    def navigate(self):
        self.driver.get(self.americanas_url)

    def close_oferta_relampago(self):
        try:
            if self.is_element_displayed(*self.close_oferta_relampago_button_class) and self.is_element_enabled(*self.close_oferta_relampago_button_class):
                self.wait_for_element_to_be_clickable(*self.close_oferta_relampago_button_class)
                return True
            return False
        except Exception:
            return False
 
    def get_email(self):
        handle_da_americanas = self.driver.current_window_handle
        return EmailPage(self.driver, handle_da_americanas)


    def click_login(self):
        self.wait_for_element_to_be_clickable(*self.login_button_class_name)
        time.sleep(1)
        return LoginPage(self.driver)
    
    def validate_home_page(self):
        assert self.driver.current_url == self.americanas_url
        