from pages_mobile.home_page import HomePage

def test_main(mobile_driver, product_data_from_api, load_data):

    product_data = product_data_from_api(index=2) 

    product_name = product_data["name"]
    product_price = product_data["price"]
    product_zipcode = product_data["zipcode"]
    delivery_estimate = product_data["delivery_estimate"]
    product_shipping_fee = product_data["shipping_fee"]
    cleaned_product_price = product_price.replace('.', '').replace(',', '.') 
   

    home_page = HomePage(mobile_driver)
    home_page.click_search_bar()
    home_page.search_for_product(product_name)

# cellphone
    # product_page = home_page.click_product_cellphone()
    # assert product_name == product_page.validate_name_product_cellphone()
    # assert product_price in product_page.validate_price_product_cellphone()
    # product_page.swipe_down()
    # product_page.input_wrong_zipcode(load_data["wrong_zipcode"])
    # product_page.click_calculate_button()
    # product_page.validate_alert_zipcode()
    # product_page.click_button_erase_cep()
    # product_page.input_correct_zipcode(product_zipcode)
    # product_page.click_calculate_button()
    # shipping_info_cellhpone = product_page.get_shipping_info_cellphone()
    # assert delivery_estimate in shipping_info_cellhpone["delivery_time"]
    # assert product_shipping_fee in shipping_info_cellhpone["shipping_cost"]
    # product_page.click_buy_button()
    # assert product_name in product_page.validate_name_and_price_cellphone()
    # assert product_price in product_page.validate_name_and_price_cellphone()
    # product_page.click_button_increase_quantity()
    # product_page.validate_product_quantity_2()
    # product_page.click_button_decrease_quantity()
    # product_page.validate_product_quantity_1()
    # product_page.click_button_increase_quantity()
    # product_page.click_button_add()

    # cart_page = product_page.click_button_cart()
    # assert product_name == cart_page.validate_product_name_cellphone()
    # product_page.validate_product_quantity_2()
    # assert float(cleaned_product_price) * 2 == cart_page.validate_price_cellphone()  
    # assert float(cleaned_product_price) * 2 == cart_page.validate_product_price_proceed_to_checkout_cellphone()

    # product_page.click_button_erase_cep()

    # cart_page.input_wrong_zipcode(load_data["wrong_zipcode"])

    # product_page.click_calculate_button()
    # product_page.validate_alert_zipcode()
    # product_page.click_button_erase_cep()

    # cart_page.input_correct_zipcode(product_zipcode)

    # product_page.click_calculate_button()
    
    # shipping_info_cellphone_cart_page = cart_page.get_shipping_info_cellphone()
    # assert delivery_estimate in shipping_info_cellphone_cart_page["delivery_time"]
    # # assert product_shipping_fee in shipping_info_cellphone_cart_page["shipping_cost"]
    # cart_page.click_button_checkout_cellphone()
    # cart_page.validate_message_enter_email_to_continue()





#watch
    # product_page = home_page.click_product_watch()
    # assert product_name == product_page.validate_name_product_watch()
    # assert product_price in product_page.validate_price_product_watch()
    # product_page.swipe_down()
    # product_page.input_wrong_zipcode(load_data["wrong_zipcode"])
    # product_page.click_calculate_button()
    # product_page.validate_alert_zipcode()
    # product_page.click_button_erase_cep()
    # product_page.input_correct_zipcode(product_zipcode)
    # product_page.click_calculate_button()
    # shipping_info_watch = product_page.get_shipping_info_watch()
    # assert delivery_estimate in shipping_info_watch["delivery_time"]
    # assert product_shipping_fee in shipping_info_watch["shipping_cost"]
    # product_page.click_buy_button()
    # assert product_name in product_page.validate_name_and_price_watch()
    # assert product_price in product_page.validate_name_and_price_watch()
    # product_page.click_button_increase_quantity()
    # product_page.validate_product_quantity_2()
    # product_page.click_button_decrease_quantity()
    # product_page.validate_product_quantity_1()
    # product_page.click_button_increase_quantity()
    # product_page.click_button_add()

    # cart_page = product_page.click_button_cart()
    # assert product_name == cart_page.validate_product_name_watch()
    # product_page.validate_product_quantity_2()
    # assert float(cleaned_product_price) * 2 == cart_page.validate_price_watch()  
    # assert float(cleaned_product_price) * 2 == cart_page.validate_product_price_proceed_to_checkout_watch()

    # product_page.click_button_erase_cep()

    # cart_page.input_wrong_zipcode(load_data["wrong_zipcode"])

    # product_page.click_calculate_button()
    # product_page.validate_alert_zipcode()
    # product_page.click_button_erase_cep()

    # cart_page.input_correct_zipcode(product_zipcode)

    # product_page.click_calculate_button()
    
    # shipping_info_watch_cart_page = cart_page.get_shipping_info_watch()
    # assert delivery_estimate in shipping_info_watch_cart_page["delivery_time"]
    # #assert product_shipping_fee in shipping_info_watch_cart_page["shipping_cost"]
    # cart_page.click_button_checkout_watch()
    # cart_page.validate_message_enter_email_to_continue()

#macbook
    product_page = home_page.click_product_macbook()
    assert product_name == product_page.validate_name_product_macbook()
    assert product_price in product_page.validate_price_product_macbook()
    product_page.swipe_down()
    product_page.input_wrong_zipcode(load_data["wrong_zipcode"])
    product_page.click_calculate_button()
    product_page.validate_alert_zipcode()
    product_page.click_button_erase_cep()
    product_page.input_correct_zipcode(product_zipcode)
    product_page.click_calculate_button()
    shipping_info_macbook = product_page.get_shipping_info_macbook()
    assert delivery_estimate in shipping_info_macbook["delivery_time"]
    assert product_shipping_fee in shipping_info_macbook["shipping_cost"]
    product_page.click_buy_button()
    assert product_name in product_page.validate_name_and_price_macbook()
    assert product_price in product_page.validate_name_and_price_macbook()
    product_page.click_button_increase_quantity()
    product_page.validate_product_quantity_2()
    product_page.click_button_decrease_quantity()
    product_page.validate_product_quantity_1()
    product_page.click_button_increase_quantity()
    product_page.click_button_add()

    cart_page = product_page.click_button_cart()
    assert product_name == cart_page.validate_product_name_macbook()
    product_page.validate_product_quantity_2()
    assert float(cleaned_product_price) * 2 == cart_page.validate_price_macbook()  
    assert float(cleaned_product_price) * 2 == cart_page.validate_product_price_proceed_to_checkout_macbook()

    product_page.click_button_erase_cep()

    cart_page.input_wrong_zipcode(load_data["wrong_zipcode"])

    product_page.click_calculate_button()
    product_page.validate_alert_zipcode()
    product_page.click_button_erase_cep()

    cart_page.input_correct_zipcode(product_zipcode)

    product_page.click_calculate_button()
    
    shipping_info_watch_cart_page = cart_page.get_shipping_info_macbook()
    assert delivery_estimate in shipping_info_watch_cart_page["delivery_time"]
    #assert product_shipping_fee in shipping_info_macbook_cart_page["shipping_cost"]
    cart_page.click_button_checkout_macbook()
    cart_page.validate_message_enter_email_to_continue()
    