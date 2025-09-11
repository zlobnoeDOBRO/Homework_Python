from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка браузера Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

try:
    # 1. Перейти на страницу
    print("Переходим на страницу...")
    driver.get("http://the-internet.herokuapp.com/inputs")

    # 2. Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")
    print("Поле ввода найдено!")

    # 3. Ввести в поле текст "Sky"
    input_field.send_keys("Sky")
    print("Введен текст: Sky")
    time.sleep(1)

    # 4. Очистить поле
    input_field.clear()
    print("Поле очищено!")
    time.sleep(1)

    # 5. Ввести в поле текст "Pro"
    input_field.send_keys("Pro")
    print("Введен текст: Pro")
    time.sleep(1)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 6. Закрыть браузер
    driver.quit()
    print("Браузер закрыт.")
