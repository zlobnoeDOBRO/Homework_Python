from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка опций Chrome (для игнорирования SSL ошибок)
chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

# Настройка браузера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

# 1. Перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# 2. Найти синюю кнопку по CSS-классу
# Кнопка имеет класс 'btn-primary'
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

# 3. Кликнуть на синюю кнопку
blue_button.click()

# Небольшая пауза чтобы увидеть результат
time.sleep(2)

# Закрыть браузер
driver.quit()
