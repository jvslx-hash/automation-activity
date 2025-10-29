from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
import time

class ProductPageApi(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_name = (By.XPATH, "//h1[contains(@class, 'ProductInfoCenter_title__hdTX_')]")
        self.product_price = (By.XPATH, "//div[contains(@class, 'ProductPrice_productPrice__vpgdo')]")
    
    def validate_product_name(self):
        return self.find_element(*self.product_name).text
    
    def validate_product_price(self):
        return self.find_element(*self.product_price).text.split()