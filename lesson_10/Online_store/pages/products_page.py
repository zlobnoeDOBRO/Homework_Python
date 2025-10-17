import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    """
    Класс для работы со страницей товаров интернет-магазина
    Содержит методы для добавления товаров в корзину и навигации
    """
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы товаров
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар в корзину по локатору: {locator}")
    def add_product_to_cart(self, locator: str) -> 'ProductsPage':
        """
        Универсальный метод для добавления товара в корзину по локатору
        
        Args:
            locator (str): ID локатора кнопки добавления товара
            
        Returns:
            ProductsPage: Инстанс текущей страницы
        """
        add_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, locator)))
        add_button.click()
        return self

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> 'ProductsPage':
        """
        Метод для перехода в корзину покупок
        
        Returns:
            ProductsPage: Инстанс текущей страницы
        """
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_list")))
        return self

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> int:
        """
        Метод для получения количества товаров в корзине
        
        Returns:
            int: Количество товаров в корзине
        """
        cart_badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)