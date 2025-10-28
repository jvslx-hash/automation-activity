from pages_web.home_page import HomePage
import pytest

def test_main(driver, load_data):

    home_page = HomePage(driver)
    home_page.navigate()
    home_page.close_oferta_relampago()

    email_page = home_page.get_email()
    email_page.open_temp_mail_in_new_tab()
    email_page.get_email_text()
    email_capturado = email_page.get_email_text()
    email_page.return_to_americanas()

    login_page = home_page.click_login()
    login_page.fill_email_field(email_capturado)
    login_page.click_send_email()

    email_page.return_to_email()
    email_page.click_message()
    email_page.get_confirmation_code()
    token_capturado = email_page.get_confirmation_code()
    email_page.return_to_americanas()

    login_page.fill_token_field(token_capturado)
    login_page.click_send_token()

    assert email_capturado in login_page.email_message()
    home_page.validate_home_page()

    my_account_page = login_page.click_my_account()

    assert email_capturado in my_account_page.validate_email_on_my_account()

    my_account_page.click_authentication_button()
    my_account_page.click_define_password_button()

    email_page.return_to_email()
    email_page.click_message_password()
    email_page.get_confirmation_code_password()
    token_senha = email_page.get_confirmation_code_password()
    email_page.return_to_americanas()

    my_account_page.fill_token_password_field(token_senha)
    my_account_page.fill_form_password_with_less_than_eight_characters(load_data["password_with_less_than_eight_characters"])
    my_account_page.fill_form_password_without_numbers(load_data["password_without_numbers"])
    my_account_page.fill_form_password_without_lowercase(load_data["password_without_lowercase"])
    my_account_page.fill_form_password_without_uppercase(load_data["password_without_uppercase"])   
    my_account_page.fill_form_correct_password(load_data["correct_password"]) 
    my_account_page.click_save_password()
    my_account_page.validate_masked_password()
    


    

    