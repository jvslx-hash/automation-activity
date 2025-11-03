from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ultils.logger import log


class BasePage:
    def __init__(self, mobile_driver):
        self.driver = mobile_driver
        self.wait = WebDriverWait(mobile_driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click_element(self, by, locator):
        log.info(f"Clicking element with locator: {locator}")
        try:
            self.find_element(by, locator).click()
            log.info("Element clicked successfully.")
        except Exception as e:
            log.error(f"Failed to click element with locator: {locator}", exc_info=True)
            raise

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
        return self.wait.until(EC.element_to_be_clickable((by, locator)))