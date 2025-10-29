from selenium.webdriver.common.by import By
from pages_web.base_page import BasePage
import time
from pages_web.view_products_page_api import ViewProductsPageApi

class HomePageApi(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.americanas_url = "https://www.americanas.com.br/"
        self.close_oferta_relampago_button_class = (By.CLASS_NAME, "show-element")
        self.search_bar = (By.ID, "search-input")
        self.preview_product_name = (By.XPATH, "//h3[contains(@class, 'SearchProducts_productName__24a3T')]")
        self.preview_product_price = (By.XPATH, "//h2[contains(@class, 'SearchProducts_productPrice__MjqHh')]")
        self.button_search = (By.XPATH, "//button[@data-testid='fs-search-button']")

    def navigate(self):
        self.driver.get(self.americanas_url)

    def close_oferta_relampago(self):
        if self.is_element_displayed(*self.close_oferta_relampago_button_class) and self.is_element_enabled(*self.close_oferta_relampago_button_class):
            self.wait_for_element_to_be_clickable(*self.close_oferta_relampago_button_class)
            return True
            
        return False
     

    def click_search_bar(self):
        self.wait_for_element_to_be_clickable(*self.search_bar)
        time.sleep(1)

    def search_for_product(self, product_name): 
        self.send_keys_to_element(*self.search_bar, product_name)
        time.sleep(1)      

    def return_preview_product_name(self):
        return self.find_element(*self.preview_product_name).text
    
    def return_preview_product_price(self):
        return self.find_element(*self.preview_product_price).text
    
    def click_to_search(self):
        self.wait_for_element_to_be_clickable(*self.button_search)
        return ViewProductsPageApi(self.driver)

