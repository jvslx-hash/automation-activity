from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def send_keys_to_element(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)
        

    def get_element_text(self, by, locator):
        return self.find_element(by, locator).text

    def is_element_displayed(self, by, locator):
        try:
            return self.find_element(by, locator).is_displayed()
        except:
            return False
        
    def is_element_enabled(self, by, locator):
        return self.find_element(by, locator).is_enabled    
    
    def wait_for_visibility_of_element(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator))).click()