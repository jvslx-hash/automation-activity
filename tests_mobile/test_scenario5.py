from pages_mobile.home_page import HomePage

def test_main(mobile_driver, product_data_from_api):

    product_data = product_data_from_api(index=2) 

    product_name = product_data["name"]
    product_price = product_data["price"]
   
    home_page = HomePage(mobile_driver)
    home_page.click_search_bar()
    home_page.search_for_product_grid(product_name)
    assert product_name in home_page.validate_product(product_name)
    assert product_price in home_page.validate_product(product_name)
    home_page.click_list_view_button()
    assert product_name in home_page.validate_product(product_name)
    assert product_price in home_page.validate_product(product_name)

    product_page = home_page.click_product_by_name(product_name)
    product_page.validate_product_name_on_page(product_name)
    product_page.validate_product_price_on_page(product_price)

