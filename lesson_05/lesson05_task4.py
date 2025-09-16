from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка браузера Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

# 1. Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")

# 2. Найти поле username и ввести значение
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_field.send_keys("tomsmith")

# 3. Найти поле password и ввести значение
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys("SuperSecretPassword!")

# 4. Найти и нажать кнопку Login
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
login_button.click()

# 5. Найти и проверить текст с зеленой плашки
success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "flash"))
)
message_text = success_message.get_attribute("textContent").strip()
assert "You logged into a secure area!" in message_text

# 6. Закрыть браузер
driver.quit()
