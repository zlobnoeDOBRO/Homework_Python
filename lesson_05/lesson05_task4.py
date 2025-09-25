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

# 1. Перейти на страницу авторизации
driver.get("http://the-internet.herokuapp.com/login")

# 2. Найти поле username и ввести значение
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
time.sleep(1)

# 3. Найти поле password и ввести значение
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
time.sleep(1)

# 4. Найти и нажать кнопку Login
login_button = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
time.sleep(2)  # Пауза для загрузки страницы после авторизации

# 5. Найти и вывести текст с зеленой плашки
success_message = driver.find_element(By.ID, "flash")
message_text = success_message.get_attribute("textContent").strip()

# 6. Закрыть браузер
driver.quit()
