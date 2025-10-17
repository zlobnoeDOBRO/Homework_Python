import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа
    """
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить поле {locator} значением {filling}")
    def enter_smth_in_field(self, filling: str, locator: str) -> 'CheckoutPage':
        """
        Универсальный метод для заполнения поля ввода
        
        Args:
            filling (str): Значение для заполнения
            locator (str): ID локатора поля ввода
            
        Returns:
            CheckoutPage: Инстанс текущей страницы
        """
        field = self.wait.until(
            EC.element_to_be_clickable((By.ID, locator)))
        field.clear()
        field.send_keys(filling)
        return self

    @allure.step("Нажать кнопку продолжения оформления заказа")
    def click_continue(self) -> 'CheckoutPage':
        """
        Метод для клика на кнопку продолжения оформления заказа
        
        Returns:
            CheckoutPage: Инстанс текущей страницы
        """
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")))
        return self

    @allure.step("Заполнить информацию о покупателе")
    def fill_checkout_info(self, checkout_fields: dict) -> 'CheckoutPage':
        """
        Метод для заполнения всей информации о покупателе
        
        Args:
            checkout_fields (dict): Словарь с данными для заполнения
            
        Returns:
            CheckoutPage: Инстанс текущей страницы
        """
        for key, value in checkout_fields.items():
            self.enter_smth_in_field(value, key)
        self.click_continue()
        return self

    @allure.step("Получить общую сумму заказа")
    def get_total_price(self) -> float:
        """
        Метод для получения общей суммы заказа
        
        Returns:
            float: Общая сумма заказа
        """
        total_element = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return float(total_amount)

    @allure.step("Завершить оформление заказа")
    def finish_checkout(self) -> 'CheckoutPage':
        """
        Метод для завершения оформления заказа
        
        Returns:
            CheckoutPage: Инстанс текущей страницы
        """
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        return self