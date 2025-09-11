from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка браузера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

try:
    # 1. Перейти на страницу
    driver.get("http://uitestingplayground.com/classattr")

    # 2. Найти синюю кнопку по CSS-классу
    # У кнопки есть класс 'btn-primary'
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

    # 3. Кликнуть на синюю кнопку
    blue_button.click()
    print("Успешно кликнули на синюю кнопку!")

    # Небольшая пауза чтобы увидеть результат
    time.sleep(2)
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрыть браузер
    driver.quit()
