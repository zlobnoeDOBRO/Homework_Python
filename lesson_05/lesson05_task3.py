from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  Настройка браузера Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

#  1. Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

#  2. Найти поле ввода (ожидаем появления элемента)
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "input"))
)

#  3. Ввести в поле текст "Sky"
input_field.send_keys("Sky")

#  4. Очистить поле
input_field.clear()

#  5. Ввести в поле текст "Pro"
input_field.send_keys("Pro")

#  6. Закрыть браузер
driver.quit()
