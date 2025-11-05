from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time

class CartPage(BasePage):
    class Locators:
        product_price = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Por R$')]")
        checkout_button = (AppiumBy.XPATH, "//android.view.View[starts-with(@content-desc, 'fechar pedido')]")
        zipcode_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='Digite o CEP']")
        delivery_and_shipping_label = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Receba em até')]")
        message_enter_email_to_continue = (AppiumBy.ACCESSIBILITY_ID, "Informe seu e-mail para continuar")


    def __init__(self, driver):
        super().__init__(driver)

    def validate_product_name(self, expected_name: str):
        product_locator = (AppiumBy.XPATH, f"//*[contains(@content-desc, '{expected_name}')]")
        assert self.is_element_displayed(*product_locator) 

    def get_product_price(self): 
        full_text = self.find_element(*self.Locators.product_price).get_attribute("content-desc") 
        valor_descontado = full_text.split('\n')[-1].split(' ')[-1] # Ex: "10.598,00"
        cleaned_price = (
            valor_descontado
            .replace('R$', '')      
            .replace('\xa0', '')   
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def get_checkout_price(self):
        full_text = self.find_element(*self.Locators.checkout_button).get_attribute("content-desc") 
        price_string = full_text.split('\n')[1]
        cleaned_price = (
            price_string
            .replace('R$', '')     
            .strip()              
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def input_wrong_zipcode(self, data):
        self.click_element(*self.Locators.zipcode_field)
        self.send_keys_to_element(*self.Locators.zipcode_field, data["zipcode"])
        time.sleep(1)

    def input_correct_zipcode(self, product_zipcode): 
        self.click_element(*self.Locators.zipcode_field)
        self.send_keys_to_element(*self.Locators.zipcode_field, product_zipcode)      

    def click_button_checkout(self):
        self.click_element(*self.Locators.checkout_button)    
        time.sleep(1)
        
    def get_shipping_info(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }   

    def validate_message_enter_email_to_continue(self):
        assert self.is_element_displayed(*self.Locators.message_enter_email_to_continue)
        
    



        
