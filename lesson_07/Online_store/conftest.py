import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
