from selenium import webdriver
import pytest
import json
from pathlib import Path
import requests
 
@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome()
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

    wishlist_url = f"{base_url}/wishlists/1/products"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(wishlist_url, headers=headers)
    response.raise_for_status()
        
    api_data = response.json()
    #print(f"DEBUG: JSON recebido de /wishlists: {api_data}")

    first_product = api_data[0]

    product_to_test = {
        "name": first_product["Product"],
        "price": first_product["Price"]
    }
        
    return product_to_test
        