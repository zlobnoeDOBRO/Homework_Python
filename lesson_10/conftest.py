import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера
    - доступна во всех тестах lesson_10
    
    Returns:
        WebDriver: Инстанс Chrome WebDriver
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_enabled": False
    })

    # Автоматическая установка и использование ChromeDriver
    service = ChromeService(ChromeDriverManager(driver_version="141.0.7390.108").install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def calculator_page(driver):
    """
    Фикстура для страницы калькулятора
    
    Args:
        driver: WebDriver instance
        
    Returns:
        SlowCalculatorPage: Инициализированная страница калькулятора
    """
    # Импорт внутри функции чтобы избежать циклических импортов
    from Calculator.pages.slow_calculator_page import SlowCalculatorPage
    
    page = SlowCalculatorPage(driver)
    page.open()
    return page