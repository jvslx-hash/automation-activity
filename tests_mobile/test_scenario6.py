from pages_mobile.home_page import HomePage

def test_main(mobile_driver, load_data):
   
    home_page = HomePage(mobile_driver)

    account_page = home_page.click_account_page()
    account_page.click_enter_with_email_button()
    account_page.click_confirm_enter_with_email_button()
    account_page.input_email(load_data["email_enter_with_email_and_password"])
    account_page.input_password(load_data["password_enter_with_email_and_password"])
    account_page.click_login_button()
    account_page.validate_change_password_button_is_displayed()



