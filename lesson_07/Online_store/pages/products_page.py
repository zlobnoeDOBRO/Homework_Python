from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Класс для работы со страницей товаров интернет-магазина
# Содержит методы для добавления товаров в корзину и навигации
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Универсальный метод для добавления товара в корзину по локатору
    def add_product_to_cart(self, locator):
        add_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, locator)))
        add_button.click()
        return self

    # Метод для перехода в корзину покупок
    def go_to_cart(self):
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")))
        return self

    # Метод для получения количества товаров в корзине
    def get_cart_count(self):
        cart_badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
