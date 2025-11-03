from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
import time

class CartPage(BasePage):
    class Locators:
        product_name_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Apple iPhone 15 de 128GB - Preto")
        product_name_watch = (AppiumBy.ACCESSIBILITY_ID, "Apple Watch Ultra 2 gps + Cellular Caixa preta de titânio de 49 mm Pulseira loop Alpina verde-escura – P")
        product_name_macbook = (AppiumBy.ACCESSIBILITY_ID, "Apple MacBook Air 13, M3, cpu de 8 núcleos, gpu de 8 núcleos, 24GB ram, 512GB ssd - Meia-noite")
        product_price_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Cor: Preto\nDe R$ 12.187,70\nPor R$ 10.598,00")
        product_price_watch = (AppiumBy.ACCESSIBILITY_ID, "De R$ 22.146,70\nPor R$ 19.558,00")
        product_price_macbook = (AppiumBy.ACCESSIBILITY_ID, "De R$ 42.110,70\nPor R$ 37.178,00")
        product_price_proceed_to_checkout_cellphone = (AppiumBy.ACCESSIBILITY_ID, "fechar pedido\nR$ 10.598,00")
        product_price_proceed_to_checkout_watch = (AppiumBy.ACCESSIBILITY_ID, "fechar pedido\nR$ 19.558,00")
        product_price_proceed_to_checkout_macbook = (AppiumBy.ACCESSIBILITY_ID, "fechar pedido\nR$ 37.178,00")
        zipcode_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='Digite o CEP']")
        delivery_and_shipping_label_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 12 dias úteis: R$ 64,00")
        delivery_and_shipping_label_watch = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 14 dias úteis: R$ 97,52")
        delivery_and_shipping_label_macbook = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 14 dias úteis: R$ 157,71")
        message_enter_email_to_continue = (AppiumBy.ACCESSIBILITY_ID, "Informe seu e-mail para continuar")


        
    def __init__(self, driver):
        super().__init__(driver)

    def validate_product_name_cellphone(self):
        return self.find_element(*self.Locators.product_name_cellphone).get_attribute("content-desc") 
    
    def validate_product_name_watch(self):
        return self.find_element(*self.Locators.product_name_watch).get_attribute("content-desc") 
    
    def validate_product_name_macbook(self):
        return self.find_element(*self.Locators.product_name_macbook).get_attribute("content-desc")

    def validate_price_cellphone(self): 
        full_text = self.find_element(*self.Locators.product_price_cellphone).get_attribute("content-desc") 
        valor_descontado = full_text.split('\n')[-1].split(' ')[-1] #"10.598,00"
        cleaned_price = (
            valor_descontado
            .replace('R$', '')      
            .replace('\xa0', '')   
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def validate_price_watch(self): 
        full_text = self.find_element(*self.Locators.product_price_watch).get_attribute("content-desc") 
        valor_descontado = full_text.split('\n')[-1].split(' ')[-1] 
        cleaned_price = (
            valor_descontado
            .replace('R$', '')      
            .replace('\xa0', '')   
            .replace('.', '')      
            .replace(',', '.')    
        )
        return float(cleaned_price)
    
    def validate_price_macbook(self): 
        full_text = self.find_element(*self.Locators.product_price_macbook).get_attribute("content-desc") 
        valor_descontado = full_text.split('\n')[-1].split(' ')[-1] 
        cleaned_price = (
            valor_descontado
            .replace('R$', '')      
            .replace('\xa0', '')   
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def validate_product_price_proceed_to_checkout_cellphone(self):
        full_text = self.find_element(*self.Locators.product_price_proceed_to_checkout_cellphone).get_attribute("content-desc") 
        price_string = full_text.split('\n')[1]
        cleaned_price = (
            price_string
            .replace('R$', '')     
            .strip()              
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def validate_product_price_proceed_to_checkout_watch(self):
        full_text = self.find_element(*self.Locators.product_price_proceed_to_checkout_watch).get_attribute("content-desc") 
        price_string = full_text.split('\n')[1]
        cleaned_price = (
            price_string
            .replace('R$', '')     
            .strip()              
            .replace('.', '')      
            .replace(',', '.')     
        )
        return float(cleaned_price)
    
    def validate_product_price_proceed_to_checkout_macbook(self):
        full_text = self.find_element(*self.Locators.product_price_proceed_to_checkout_macbook).get_attribute("content-desc") 
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

    def click_button_checkout_cellphone(self):
        self.click_element(*self.Locators.product_price_proceed_to_checkout_cellphone)    
        time.sleep(1)

    def click_button_checkout_watch(self):
        self.click_element(*self.Locators.product_price_proceed_to_checkout_watch) 
        time.sleep(1)

    def click_button_checkout_macbook(self):
        self.click_element(*self.Locators.product_price_proceed_to_checkout_macbook)   
        time.sleep(1)      
        
    def get_shipping_info_cellphone(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label_cellphone).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }    
    
    def get_shipping_info_watch(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label_watch).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }   
    
    def get_shipping_info_macbook(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label_macbook).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }   

    def validate_message_enter_email_to_continue(self):
        assert self.is_element_displayed(*self.Locators.message_enter_email_to_continue)
        
    



        
