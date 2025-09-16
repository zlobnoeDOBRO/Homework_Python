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

    # 5. Нажимаем на кнопки калькулятора: 7 + 8 =
    button_7 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
    )
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    # 6. Ждем появления результата "15" на экране калькулятора
    # Используем явное ожидание, которое будет ждать до 46 секунд
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # 7. Получаем текст из дисплея калькулятора и проверяем результат
    screen_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    result_text = screen_element.text

    assert result_text == "15", (
        f"Ожидаемый результат: 15, фактический результат: {result_text}"
    )

    # 8. Закрываем браузер
    driver.quit()
