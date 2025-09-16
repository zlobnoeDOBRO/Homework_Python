from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройка опций Chrome для игнорирования SSL ошибок
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Настройка браузера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

# 1. Перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# 2. Найти и дождаться кликабельности синей кнопки
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
)

# 3. Кликнуть на синюю кнопку
blue_button.click()

# 4. Проверка
assert blue_button is not None

# Закрыть браузер
driver.quit()
