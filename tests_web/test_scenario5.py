from pages_web.home_page_api import HomePageApi

def test_main(driver, product_data_from_api):

    product_data = product_data_from_api(index=1) 

    product_name = product_data["name"]
    product_price = product_data["price"]

    home_page_api = HomePageApi(driver)
    home_page_api.navigate()
    home_page_api.close_oferta_relampago()
    home_page_api.click_search_bar()
    home_page_api.search_for_product(product_name)
    assert home_page_api.return_preview_product_name() == product_name
    assert product_price in home_page_api.return_preview_product_price()

    view_products_page_api = home_page_api.click_to_search()
    assert view_products_page_api.validate_product_name_grid_view() == product_name
    assert product_price in view_products_page_api.validate_product_price_grid_view()
    view_products_page_api.change_to_list()
    assert view_products_page_api.validate_product_name_list_view() == product_name
    assert product_price in view_products_page_api.validate_product_price_list_view()
    
    product_page_api = view_products_page_api.click_open_product()
    assert product_page_api.validate_product_name() == product_name
    assert product_price in product_page_api.validate_product_price()