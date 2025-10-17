import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины покупок
    """
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> 'CartPage':
        """
        Метод для клика на кнопку продолжения оформления заказа
        
        Returns:
            CartPage: Инстанс текущей страницы
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        return self

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Метод для получения количества товаров в корзине
        
        Returns:
            int: Количество товаров в корзине
        """
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)