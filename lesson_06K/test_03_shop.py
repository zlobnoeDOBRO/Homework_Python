from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestShop:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Используем Firefox как указано в задании
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_shopping_cart_total(self):
        # Открываем сайт магазина
        self.driver.get("https://www.saucedemo.com/")

        # Авторизуемся как standard_user
        username_field = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "user-name")))
        username_field.send_keys("standard_user")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # Ждем загрузки страницы с товарами
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item"))
            )

        # Добавляем товары в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            # Находим кнопку добавления для каждого товара
            add_button = self.driver.find_element(
                By.XPATH,
                (f"//div[contains(text(), '{product_name}')]"
                 f"/ancestor::div[@class='inventory_item']"
                 f"//button[contains(text(), 'Add to cart')]")
            )
            add_button.click()

        # Переходим в корзину
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ждем загрузки корзины
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "cart_item")))

        # Нажимаем Checkout
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Ждем загрузки формы
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        # Заполняем форму данными
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Иван")

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")

        zip_code_field = self.driver.find_element(By.ID, "postal-code")
        zip_code_field.send_keys("123456")

        # Нажимаем Continue
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Ждем загрузки страницы с итоговой стоимостью
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))

        # Читаем итоговую стоимость
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")

        # Проверяем, что итоговая сумма равна $58.29
        assert total_amount == "58.29", (
            f"Итоговая сумма должна быть $58.29, "
            f"но получилось ${total_amount}"
        )
