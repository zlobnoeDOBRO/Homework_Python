# Импортируем необходимые модули из Selenium и других библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_delay():
    # 1. Инициализация веб-драйвера для браузера Google Chrome
    driver = webdriver.Chrome()

    # 2. Открываем страницу калькулятора
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # 3. Настройка ожидания WebDriverWait с таймаутом 45 секунд
    wait = WebDriverWait(driver, 45)

    # 4. Ожидаем появления поля ввода задержки и вводим значение 45
    delay_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_field.clear()
    delay_field.send_keys("45")

    # 5. Находим все кнопки сразу после загрузки поля ввода
    driver.find_elements(By.CSS_SELECTOR, ".btn-outline-primary")

    # Нажимаем на кнопки калькулятора: 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 6. Ждем появления результата "15" на экране калькулятора.
    assert wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # 7. Закрываем браузер
    driver.quit()
