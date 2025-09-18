from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка браузера Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

# 1. Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# 2. Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# 3. Ввести в поле текст "Sky"
input_field.send_keys("Sky")
time.sleep(1)

# 4. Очистить поле
input_field.clear()
time.sleep(1)

# 5. Ввести в поле текст "Pro"
input_field.send_keys("Pro")
time.sleep(1)

# 6. Закрыть браузер
driver.quit()
