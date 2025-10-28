from selenium import webdriver
import pytest
import json
from pathlib import Path


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
