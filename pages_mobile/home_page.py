from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time
from pages_mobile.product_page import ProductPage

class HomePage(BasePage):
    class Locators:
        search_bar_button = (AppiumBy.ACCESSIBILITY_ID, "busque aqui seu produto")
        search_bar_field = (AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        button_product_cellphone = (AppiumBy.ACCESSIBILITY_ID, "-13%\nApple iPhone 15 de 128GB - Preto\n R$ 6.093,85\nR$ 5.299,00\nà vista")
        button_product_watch = (AppiumBy.ACCESSIBILITY_ID, "-12%\nApple Watch Ultra 2 gps + Cellular Caixa preta de titânio de 49 mm Pulseira loop Alpina verde-escura – P\n R$ 11.073,35\nR$ 9.779,00\nà vista")
        button_product_macbook = (AppiumBy.ACCESSIBILITY_ID, "-12%\nApple MacBook Air 13, M3, cpu de 8 núcleos, gpu de 8 núcleos, 24GB ram, 512GB ssd - Meia-noite\n R$ 21.055,35\nR$ 18.589,00\nà vista")
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_bar(self):
        self.click_element(*self.Locators.search_bar_button)  

    def search_for_product(self, product_name): 
        self.send_keys_to_element(*self.Locators.search_bar_field, product_name)
        time.sleep(4)          

    def click_product_cellphone(self):    
        self.click_element(*self.Locators.button_product_cellphone) 
        time.sleep(2)
        return ProductPage(self.driver)
    
    def click_product_watch(self):    
        self.click_element(*self.Locators.button_product_watch) 
        time.sleep(2)
        return ProductPage(self.driver)
    
    def click_product_macbook(self):    
        self.click_element(*self.Locators.button_product_macbook) 
        time.sleep(2)
        return ProductPage(self.driver)

        
    
