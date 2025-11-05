from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .cart_page import CartPage
import time

class ProductPage(BasePage):
    class Locators:
        calculate_button = (AppiumBy.ACCESSIBILITY_ID, "Calcular")
        click_zipcode_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='Digite o CEP']")
        zipcode_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        button_erase_cep = (AppiumBy.ACCESSIBILITY_ID, "Apagar cep pesquisado")
        button_buy = (AppiumBy.XPATH, "//android.view.View[@content-desc='comprar']")
        button_decrease_quantity = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Reduzir quantidade em 1']")
        button_increase_quantity = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Aumentar quantidade em 1']")
        product_quantity_1 = (AppiumBy.XPATH, "//android.widget.EditText[@text='1']")
        product_quantity_2 = (AppiumBy.XPATH, "//android.widget.EditText[@text='2']") 
        button_add = (AppiumBy.ACCESSIBILITY_ID, "adicionar e continuar comprando")
        button_cart = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Carrinho']")
        alert_zipcode = (AppiumBy.ACCESSIBILITY_ID, "Frete indisponível para o CEP: 00000-000")
        delivery_and_shipping_label = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Receba em até')]") 
        text_name_and_price = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Por R$')]")

    
    def __init__(self, driver):
        super().__init__(driver)

    
    def validate_product_name_on_page(self, expected_name: str):
        product_name_locator = (AppiumBy.XPATH, f"//android.view.View[@content-desc='{expected_name}']")
        assert self.is_element_displayed(*product_name_locator)

    def validate_product_price_on_page(self, expected_price: str):
        product_price_locator = (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc, '{expected_price}')]")
        assert self.is_element_displayed(*product_price_locator)
    
    def swipe_down(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.7)
        end_y = int(size['height'] * 0.2)
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)
        time.sleep(5)

    def swipe_up(self):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.2)    
        end_y = int(size['height'] * 0.8)
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)  

    def input_wrong_zipcode(self, data):
        self.click_element(*self.Locators.click_zipcode_field)
        self.send_keys_to_element(*self.Locators.zipcode_field, data["zipcode"])

    def click_calculate_button(self):
        self.click_element(*self.Locators.calculate_button)
        
    def validate_alert_zipcode(self):
        assert self.is_element_displayed(*self.Locators.alert_zipcode)      

    def click_button_erase_cep(self):
        self.click_element(*self.Locators.button_erase_cep)    
        time.sleep(1)

    def input_correct_zipcode(self, product_zipcode): 
        self.click_element(*self.Locators.click_zipcode_field)
        self.send_keys_to_element(*self.Locators.zipcode_field, product_zipcode)  

    def get_shipping_info(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }
  
    def click_buy_button(self):
        self.click_element(*self.Locators.button_buy)
        time.sleep(1)

    def validate_name_and_price(self):
        return self.find_element(*self.Locators.text_name_and_price).get_attribute("content-desc")
    
    def click_button_increase_quantity(self):
        self.click_element(*self.Locators.button_increase_quantity)   

    def click_button_decrease_quantity(self):
        self.click_element(*self.Locators.button_decrease_quantity)     

    def validate_product_quantity_2(self):
        assert self.is_element_displayed(*self.Locators.product_quantity_2)  
    
    def validate_product_quantity_1(self):
        assert self.is_element_displayed(*self.Locators.product_quantity_1)

    def click_button_add(self):
        self.click_element(*self.Locators.button_add) 
        time.sleep(1)

    def click_button_cart(self):
        self.click_element(*self.Locators.button_cart) 
        time.sleep(1)
        return CartPage(self.driver)
    

