import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера
      - доступна во всех тестах lesson_07"""
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


@pytest.fixture
def calculator_page(driver):
    """Фикстура для страницы калькулятора"""
    # Импорт здесь чтобы избежать циклических импортов
    from Calculator.pages.slow_calculator_page import SlowCalculatorPage
    page = SlowCalculatorPage(driver)
    page.open()
    return page
