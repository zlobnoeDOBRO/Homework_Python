import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Класс для работы со страницей медленного калькулятора
    """
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        # Ожидание до 45 секунд для операций калькулятора
        self.wait = WebDriverWait(driver, 45)
        # Локаторы элементов страницы
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, "#calculator .screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открытие страницы калькулятора
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/" +
                        "slow-calculator.html")

    @allure.step("Установить задержку: {value} секунд")
    def set_delay(self, value: str) -> None:
        """
        Установка времени задержки вычислений в секундах
        
        Args:
            value (str): Время задержки в секундах
        """
        delay_elem = self.driver.find_element(*self.delay_input)
        delay_elem.clear()
        delay_elem.send_keys(value)

    @allure.step("Нажать кнопку: {label}")
    def click_button(self, label: str) -> None:
        """
        Универсальный метод для нажатия любой кнопки калькулятора
        
        Args:
            label (str): Текст на кнопке калькулятора
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{label}']").click()

    @allure.step("Получить результат с экрана калькулятора")
    def get_result(self) -> str:
        """
        Получение текущего текста с экрана калькулятора
        
        Returns:
            str: Текст результата на экране калькулятора
        """
        return self.driver.find_element(*self.screen).text

    @allure.step("Ожидать результат: {expected_result}")
    def wait_for_result(self, expected_result: str) -> None:
        """
        Ожидание появления ожидаемого результата на экране
        
        Args:
            expected_result (str): Ожидаемый текст результата
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.screen, expected_result))