from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time
from pages_mobile.product_page import ProductPage
from pages_mobile.account_page import AccountPage

class HomePage(BasePage):
    class Locators:
        search_bar_button = (AppiumBy.XPATH, "//*[@content-desc='busque aqui seu produto']")
        search_bar_field = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        list_view_button = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView[2]")
        account_page_button = (AppiumBy.ACCESSIBILITY_ID, "Conta\nTab 5 of 5")
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_bar(self):
        self.click_element(*self.Locators.search_bar_button)  

    def search_for_product(self, product_name): 
        self.send_keys_to_element(*self.Locators.search_bar_field, product_name)
        time.sleep(4)          

    def click_product_by_name(self, product_name):
        product_locator = (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc, '{product_name}')]")
        
        self.click_element(*product_locator) 
        time.sleep(2)
        return ProductPage(self.driver)
    
    # scenario 5

    def search_for_product_grid(self, product_name):
        self.send_keys_to_element(*self.Locators.search_bar_field, product_name)
        time.sleep(0.5)
        self.driver.press_keycode(66)

    def validate_product(self, product_name):
        product_locator = (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc, '{product_name}')]")
        element = self.find_element(*product_locator)
        return element.get_attribute("content-desc")
    
    def click_list_view_button(self):
        self.click_element(*self.Locators.list_view_button)  
        time.sleep(1)

    #scenario 6
    def click_account_page(self):
        self.click_element(*self.Locators.account_page_button)
        return AccountPage(self.driver)

    

        

    

        
    
