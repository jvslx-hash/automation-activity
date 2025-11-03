import pytest
import json
from pathlib import Path
import requests
from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver
from appium.options.common.base import AppiumOptions

@pytest.fixture
def driver():
    driver_instance = selenium_webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

@pytest.fixture(scope="session")
def load_data():
    """Lê o JSON e retorna como dicionário"""
    json_path = Path(__file__).parent / "data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@pytest.fixture(scope="session")
def product_data_from_api():
    
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    base_url = "http://127.0.0.1:8000"

    login_url = f"{base_url}/auth/login"
        
    login_data = {"email": auth_user, "password": auth_pass}
        
    login_response = requests.post(login_url, json=login_data)
        
    login_response.raise_for_status()

    login_json = login_response.json()
        
    token = login_json["access_token"] 

    all_products_translated = []

    wishlist_url = f"{base_url}/wishlists/1/products"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(wishlist_url, headers=headers)
    response.raise_for_status()
        
    api_data = response.json()
    #print(f"DEBUG: JSON recebido de /wishlists: {api_data}")

    for product in api_data:
        #print(f"{product}")
        all_products_translated.append({
            "name": product["Product"],
            "price": product["Price"],
            "zipcode": product["Zipcode"], 
            "delivery_estimate": product["delivery_estimate"],
            "shipping_fee": product["shipping_fee"]
        })
        
    def _get_product_by_index(index: int):
        return all_products_translated[index]

    return _get_product_by_index

# mobile



@pytest.fixture(scope="function")
def mobile_driver(request):
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({ "platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.b2w.americanas",
    "appium:autoGrantPermissions": True,
    "appium:ensureWebviewsHavePages": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appWaitDuration": 30000 }) # Capabilities defined here

    _driver = appium_webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # The 'yield' keyword passes control to the test function
    yield _driver
    if _driver:
        _driver.quit()

        