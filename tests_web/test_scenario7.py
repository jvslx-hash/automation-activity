from pages_web.home_page import HomePage

def test_main(driver, load_data):

    home_page = HomePage(driver)
    home_page.navigate()
    home_page.close_oferta_relampago()

    login_page = home_page.click_login()
    login_page.click_entrar_com_email_e_senha()
    login_page.fill_login_field(load_data["email_enter_with_email_and_password"])
    login_page.fill_password_field(load_data["wrong_password"])
    login_page.click_sign_in_button()
    login_page.validate_message_user_or_password_incorrect()

