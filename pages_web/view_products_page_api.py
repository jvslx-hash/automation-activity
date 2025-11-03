from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
from pages_web.product_page_api import ProductPageApi
import time

class ViewProductsPageApi(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_name = (By.XPATH, "//h3[contains(@class, 'ProductCard_productName__mwx7Y')]")
        self.product_price = (By.XPATH, "//p[contains(@class, 'ProductCard_productPrice__XFEqu')]")
        self.button_list = (By.XPATH, "//button[@aria-label='Forma de exibição horizontal']")

    
    def validate_product_name_grid_view(self):
        return self.find_element(*self.product_name).text
    
    
    def validate_product_price_grid_view(self):
        return self.find_element(*self.product_price).text.split()
        time.sleep(2)
    
    def change_to_list(self):
        self.wait_for_element_to_be_clickable(*self.button_list)
        time.sleep(2)

    def validate_product_name_list_view(self):
        return self.find_element(*self.product_name).text
    
    def validate_product_price_list_view(self):
        return self.find_element(*self.product_price).text.split()
    
    def click_open_product(self):
        self.scroll_to_element(*self.product_name)
        self.wait_for_element_to_be_clickable(*self.product_name)
        return ProductPageApi(self.driver)
    

    
    



