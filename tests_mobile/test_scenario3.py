from pages_mobile.home_page import HomePage
import time

def test_main(mobile_driver, product_data_from_api, load_data): 

    for product_data in product_data_from_api:

        product_name = product_data["name"]
        product_price = product_data["price"]
        product_zipcode = product_data["zipcode"]
        delivery_estimate = product_data["delivery_estimate"]
        product_shipping_fee = product_data["shipping_fee"]
        
        cleaned_product_price = product_price.replace('.', '').replace(',', '.') 
    
    
        home_page = HomePage(mobile_driver)
        home_page.click_search_bar()
        home_page.search_for_product(product_name)

        product_page = home_page.click_product_by_name(product_name)

        product_page.validate_product_name_on_page(product_name)
        product_page.validate_product_price_on_page(product_price)
        
        product_page.swipe_down()
        product_page.input_wrong_zipcode(load_data["wrong_zipcode"])
        product_page.click_calculate_button()
        product_page.validate_alert_zipcode()
        product_page.click_button_erase_cep()
        product_page.input_correct_zipcode(product_zipcode)
        product_page.click_calculate_button()

        shipping_info = product_page.get_shipping_info()
        assert delivery_estimate in shipping_info["delivery_time"]
        assert product_shipping_fee in shipping_info["shipping_cost"]
        
        product_page.click_buy_button()
    
        assert product_name in product_page.validate_name_and_price()
        assert product_price in product_page.validate_name_and_price()
        
        product_page.click_button_increase_quantity()
        product_page.validate_product_quantity_2()
        product_page.click_button_decrease_quantity()
        product_page.validate_product_quantity_1()
        product_page.click_button_increase_quantity()
        product_page.click_button_add()

        cart_page = product_page.click_button_cart()
        cart_page.validate_product_name(product_name) 
        
        product_page.validate_product_quantity_2()
        
        assert float(cleaned_product_price) * 2 == cart_page.get_product_price()
        assert float(cleaned_product_price) * 2 == cart_page.get_checkout_price()

        product_page.click_button_erase_cep()
        time.sleep(0.5)
        cart_page.input_wrong_zipcode(load_data["wrong_zipcode"])
        time.sleep(0.5)
        product_page.click_calculate_button()
        product_page.validate_alert_zipcode()
        product_page.click_button_erase_cep()
        cart_page.input_correct_zipcode(product_zipcode)
        product_page.click_calculate_button()
        
        shipping_info_cart_page = cart_page.get_shipping_info() 
        assert delivery_estimate in shipping_info_cart_page["delivery_time"]
        # assert product_shipping_fee in shipping_info_cart_page["shipping_cost"]
        
        cart_page.click_button_checkout()
        cart_page.validate_message_enter_email_to_continue()
    