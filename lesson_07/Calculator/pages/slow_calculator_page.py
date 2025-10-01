from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        # Ожидание до 45 секунд для операций калькулятора
        self.wait = WebDriverWait(driver, 45)
        # Локаторы элементов страницы
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, "#calculator .screen")

    def open(self):
        # Открытие страницы калькулятора
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/" +
                        "slow-calculator.html")

    def set_delay(self, value: str):
        # Установка времени задержки вычислений в секундах
        delay_elem = self.driver.find_element(*self.delay_input)
        delay_elem.clear()
        delay_elem.send_keys(value)

    def click_button(self, label: str):
        # Универсальный метод для нажатия любой кнопки калькулятора
        self.driver.find_element(By.XPATH, f"//span[text()='{label}']").click()

    def get_result(self) -> str:
        # Получение текущего текста с экрана калькулятора
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, expected_result: str):
        # Ожидание появления ожидаемого результата на экране
        self.wait.until(EC.text_to_be_present_in_element(
            self.screen, expected_result))
