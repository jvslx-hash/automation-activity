import requests
import pytest
BASE_URL = "http://127.0.0.1:8000"

ENDPOINTS_TO_TEST = [
    ("POST", "/wishlists"),
    ("GET", "/wishlists"),
    ("POST", "/wishlists/1/products"),
    ("GET", "/wishlists/1/products"),
    ("PUT", "/products/1"),
    ("DELETE", "/products/1")
]


def test_scenario8(): 
    email = "testuser5@example.com"
    username = "testuser5"
    
    register_url = f"{BASE_URL}/auth/register"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa123!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 200
    
    response_data = response.json()
    
    assert "id" in response_data
    assert response_data["email"] == email
    assert response_data["username"] == username
    assert "password" not in response_data

def test_scenario9(): 
    email = "testuser4@example.com"
    username = "testuser4"
    
    register_url = f"{BASE_URL}/auth/register"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa123!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 400 

    response_data = response.json()
    # print(response_data)
    assert response_data["detail"] == "Email already registered"

def test_scenario10(): 
    email = "testuser4example.com"
    username = "testuser4"
    
    register_url = f"{BASE_URL}/auth/register"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa123!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 422

    response_data = response.json()
    assert response_data["detail"] == "Invalid email format"

def test_scenario11(): 
    email = "testuser5@example.com"
    username = "testuser5"
    
    register_url = f"{BASE_URL}/auth/login"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa123!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 200

    response_data = response.json()
    print(response_data)
    assert "access_token" in response_data
    assert "token_type" in response_data

def test_scenario12(): 
    email = "testuser1@example.com"
    username = "testuser1"
    
    register_url = f"{BASE_URL}/auth/login"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa1234!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 401

    response_data = response.json()
    assert response_data["detail"] == "Incorrect email or password"

def test_scenario13(): 
    email = "santacruz@example.com"
    username = "testuser1"
    
    register_url = f"{BASE_URL}/auth/login"
    
    data = {
        "username": username,
        "email": email,
        "password": "Senhamassa1234!"
    }

    response = requests.post(register_url, json=data)
    assert response.status_code == 401

    response_data = response.json()
    assert response_data["detail"] == "Incorrect email or password"

def test_scenario14():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists"
    
    payload = {
        "name": "wishlist 3"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert "owner_id" in response_data
    assert response_data["name"] == payload["name"]
       
def test_scenario15():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists"
    
    payload = {
        "name": "wishlist 1"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 409
    response_data = response.json()
    assert response_data["message"] == "A wishlist with this name already exists"

def test_scenario16():      
    wishlist_url = f"{BASE_URL}/wishlists"
    
    payload = {
        "name": "wishlist sem autorizacao"
    }

    response = requests.post(wishlist_url, json=payload)
    assert response.status_code == 401
    response_data = response.json()
    assert response_data["detail"] == "Not authenticated"
    
def test_scenario17():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists"
    
    payload = {  
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 422
    response_data = response.json()
    assert response_data["detail"] == "Missing name"    
    
def test_scenario18():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url,headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)

def test_scenario19():  
    auth_user = "testuser4@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url,headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == []

def test_scenario20():  
    wishlist_url = f"{BASE_URL}/wishlists"
    response = requests.get(wishlist_url)
    assert response.status_code == 401
    response_data = response.json()
    print(response_data)

def test_scenario21():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products"
    
    payload = {  
        "Product": "Arruda2", "Price": "99.99", "Zipcode": "12345678", "delivery_estimate": "5 dias", "shipping_fee": "15.00"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert "wishlist_id" in response_data
    assert response_data["wishlist_id"] == 1
    assert response_data["Product"] == payload["Product"]
    assert response_data["is_purchased"] == False
     
def test_scenario22():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/99/products"
    
    payload = {  
        "Product": "Arruda", "Price": "99.99", "Zipcode": "12345678", "delivery_estimate": "5 dias", "shipping_fee": "15.00"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 404
    response_data = response.json()  
    assert response_data["detail"] == "Wishlist not found"

def test_scenario23():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products"
    
    payload = {  
        "Product": "Arruda", "Price": "99.99", "Zipcode": "12345678", "delivery_estimate": "5 dias", "shipping_fee": "15.00"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 404
    response_data = response.json()  
    assert response_data["detail"] == "Wishlist not found"

def test_scenario24():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products"
    
    payload = {  
        "Product": "Arruda"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(wishlist_url, json=payload, headers=headers)
    assert response.status_code == 422
    response_data = response.json()  
    assert response_data["detail"] == "Missing product data"

def test_scenario25():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()  
    print(response_data)
    assert isinstance(response_data, list)

def test_scenario26():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products?Product=Arruda"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url, headers=headers)
    assert response.status_code == 200

def test_scenario27():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products?is_purchased=true"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url, headers=headers)
    assert response.status_code == 200    

def test_scenario28():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    wishlist_url = f"{BASE_URL}/wishlists/1/products"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(wishlist_url, headers=headers)
    assert response.status_code == 404

def test_scenario29():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/1"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "150.00"
    }

    response = requests.put(products_url, json=payload, headers=headers)
    
    assert response.status_code == 200
    
    response_data = response.json()
    
    assert response_data["Price"] == payload["Price"]
    assert response_data["id"] == 1

def test_scenario30():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/999"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "150.00"
    }

    response = requests.put(products_url, json=payload, headers=headers)
    
    assert response.status_code == 404

def test_scenario31():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/1"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "151.00"
    }

    response = requests.put(products_url, json=payload, headers=headers)    
    assert response.status_code == 404

def test_scenario32():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/1"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "151.00"
    }

    response = requests.delete(products_url, json=payload, headers=headers)    
    assert response.status_code == 204 #ja apaguei o 1, dai a api retorna 404, ao inves de 204

def test_scenario33():  
    auth_user = "projeto@example.com"
    auth_pass = "Senha123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/999"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "151.00"
    }

    response = requests.delete(products_url, json=payload, headers=headers)    
    assert response.status_code == 404

def test_scenario34():  
    auth_user = "testuser1@example.com"
    auth_pass = "Senhamassa123!"
    login_url = f"{BASE_URL}/auth/login"
    login_data = {"email": auth_user, "password": auth_pass}
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json()["access_token"]
    
    products_url = f"{BASE_URL}/products/1"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "Price": "151.00"
    }

    response = requests.delete(products_url, json=payload, headers=headers)    
    assert response.status_code == 404



@pytest.mark.parametrize("method, endpoint_path", ENDPOINTS_TO_TEST)
def test_scenario35(method, endpoint_path):
    
    url = f"{BASE_URL}{endpoint_path}"
    response = None
    
    if method == "POST":
        response = requests.post(url, json={}) 
    elif method == "GET":
        response = requests.get(url)
    elif method == "PUT":
        response = requests.put(url, json={}) 
    elif method == "DELETE":
        response = requests.delete(url)
    elif method == "PATCH":
        response = requests.patch(url) 

    assert response.status_code == 401
    
    response_data = response.json()
    assert response_data["detail"] == "Not authenticated"

@pytest.mark.parametrize("method, endpoint_path", ENDPOINTS_TO_TEST)
def test_endpoints_with_invalid_malformed_token(method, endpoint_path):
    
    url = f"{BASE_URL}{endpoint_path}"
    
    invalid_token_header = "Bearer invalidtokenstring"
    headers = {"Authorization": invalid_token_header}
    response = None

    if method == "POST":
        response = requests.post(url, json={}, headers=headers)
    elif method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "PUT":
        response = requests.put(url, json={}, headers=headers)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)

    assert response.status_code == 401
    response_data = response.json()
    assert response_data["detail"] == "Could not validate credentials"