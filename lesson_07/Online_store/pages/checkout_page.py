from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Класс для работы со страницей оформления заказа
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Универсальный метод для заполнения поля ввода
    def enter_smth_in_field(self, filling, locator):
        field = self.wait.until(
            EC.element_to_be_clickable((By.ID, locator)))
        field.clear()
        field.send_keys(filling)
        return self

    # Метод для клика на кнопку продолжения оформления заказа
    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")))
        return self

    # Метод для заполнения всей информации о покупателе
    def fill_checkout_info(self, checkout_fields):
        for key, value in checkout_fields.items():
            self.enter_smth_in_field(value, key)
        self.click_continue()
        return self

    # Метод для получения общей суммы заказа
    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return float(total_amount)

    # Метод для завершения оформления заказа
    def finish_checkout(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        return self
