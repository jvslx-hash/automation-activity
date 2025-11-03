from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .cart_page import CartPage
import time

class ProductPage(BasePage):
    class Locators:
        product_name_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Apple iPhone 15 de 128GB - Preto")
        product_price_cellphone = (AppiumBy.ACCESSIBILITY_ID, "R$ 5.299,00")
        product_name_watch = (AppiumBy.ACCESSIBILITY_ID, "Apple Watch Ultra 2 gps + Cellular Caixa preta de titânio de 49 mm Pulseira loop Alpina verde-escura – P")
        product_price_watch = (AppiumBy.ACCESSIBILITY_ID, "R$ 9.779,00")
        product_name_macbook= (AppiumBy.ACCESSIBILITY_ID, "Apple MacBook Air 13, M3, cpu de 8 núcleos, gpu de 8 núcleos, 24GB ram, 512GB ssd - Meia-noite")
        product_price_macbook = (AppiumBy.ACCESSIBILITY_ID, "R$ 18.589,00")
        alert_zipcode = (AppiumBy.ACCESSIBILITY_ID, "Frete indisponível para o CEP: 00000-000")
        calculate_button = (AppiumBy.ACCESSIBILITY_ID, "Calcular")
        click_zipcode_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='Digite o CEP']")
        zipcode_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        delivery_and_shipping_label_macbook = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 14 dias úteis: R$ 94,60") #Mutável dependendo do json!!!!!!!!
        delivery_and_shipping_label_watch = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 14 dias úteis: R$ 64,49") #Mutável dependendo do json!!!!!!!!
        delivery_and_shipping_label_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Receba em até 12 dias úteis: R$ 48,00") #Mutável dependendo do json!!!!!!!!
        button_erase_cep = (AppiumBy.ACCESSIBILITY_ID, "Apagar cep pesquisado")
        button_buy = (AppiumBy.XPATH, "//android.view.View[@content-desc='comprar']")
        button_decrease_quantity = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Reduzir quantidade em 1']")
        button_increase_quantity = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Aumentar quantidade em 1']")
        text_name_and_price_cellphone = (AppiumBy.ACCESSIBILITY_ID, "Apple iPhone 15 de 128GB - Preto\nCor: Preto\nDe R$ 6.093,85\nPor R$ 5.299,00")
        text_name_and_price_watch = (AppiumBy.ACCESSIBILITY_ID, "Apple Watch Ultra 2 gps + Cellular Caixa preta de titânio de 49 mm Pulseira loop Alpina verde-escura – P\nDe R$ 11.073,35\nPor R$ 9.779,00")
        text_name_and_price_macbook = (AppiumBy.ACCESSIBILITY_ID, "Apple MacBook Air 13, M3, cpu de 8 núcleos, gpu de 8 núcleos, 24GB ram, 512GB ssd - Meia-noite\nDe R$ 21.055,35\nPor R$ 18.589,00")
        product_quantity_1 = (AppiumBy.XPATH, "//android.widget.EditText[@text='1']")
        product_quantity_2 = (AppiumBy.XPATH, "//android.widget.EditText[@text='2']") 
        button_add = (AppiumBy.ACCESSIBILITY_ID, "adicionar e continuar comprando")
        button_cart = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='Carrinho']")
        

    def __init__(self, driver):
        super().__init__(driver)

    def validate_name_product_cellphone(self):
        return self.find_element(*self.Locators.product_name_cellphone).get_attribute("content-desc")
    
    def validate_price_product_cellphone(self):
        return self.find_element(*self.Locators.product_price_cellphone).get_attribute("content-desc")
    
    def validate_name_product_watch(self):
        return self.find_element(*self.Locators.product_name_watch).get_attribute("content-desc")
    
    def validate_price_product_watch(self):
        return self.find_element(*self.Locators.product_price_watch).get_attribute("content-desc")
    
    def validate_name_product_macbook(self):
        return self.find_element(*self.Locators.product_name_macbook).get_attribute("content-desc")
    
    def validate_price_product_macbook(self):
        return self.find_element(*self.Locators.product_price_macbook).get_attribute("content-desc")
    
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
        time.sleep(1)

    def click_calculate_button(self):
        self.click_element(*self.Locators.calculate_button)
        

    def validate_alert_zipcode(self):
        assert self.is_element_displayed(*self.Locators.alert_zipcode)      

    def click_button_erase_cep(self):
        self.click_element(*self.Locators.button_erase_cep)    
        time.sleep(2)

    def input_correct_zipcode(self, product_zipcode): 
        self.click_element(*self.Locators.click_zipcode_field)
        self.send_keys_to_element(*self.Locators.zipcode_field, product_zipcode)  

    def get_shipping_info_macbook(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label_macbook).get_attribute("content-desc")
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
    
    def get_shipping_info_cellphone(self):
        full_text = self.find_element(*self.Locators.delivery_and_shipping_label_cellphone).get_attribute("content-desc")
        partes = full_text.split(':')
        prazo = partes[0].strip()
        frete = partes[1].strip()
        return {
            "delivery_time": prazo,
            "shipping_cost": frete
        }
    
    def click_buy_button(self):
        self.click_element(*self.Locators.button_buy)
        return CartPage(self.driver)
    
    def click_button_increase_quantity(self):
        self.click_element(*self.Locators.button_increase_quantity)   

    def click_button_decrease_quantity(self):
        self.click_element(*self.Locators.button_decrease_quantity)     

    def validate_name_and_price_cellphone(self):
        return self.find_element(*self.Locators.text_name_and_price_cellphone).get_attribute("content-desc")

    def validate_name_and_price_watch(self):
        return self.find_element(*self.Locators.text_name_and_price_watch).get_attribute("content-desc")

    def validate_name_and_price_macbook(self):
        return self.find_element(*self.Locators.text_name_and_price_macbook).get_attribute("content-desc") 

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
    

