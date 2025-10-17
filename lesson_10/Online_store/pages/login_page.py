import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей авторизации
    """
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы логина
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открытие страницы авторизации
        
        Returns:
            LoginPage: Инстанс текущей страницы
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """
        Ввод имени пользователя
        
        Args:
            username (str): Имя пользователя
            
        Returns:
            LoginPage: Инстанс текущей страницы
        """
        username_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> 'LoginPage':
        """
        Ввод пароля пользователя
        
        Args:
            password (str): Пароль пользователя
            
        Returns:
            LoginPage: Инстанс текущей страницы
        """
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> 'LoginPage':
        """
        Нажатие кнопки авторизации
        
        Returns:
            LoginPage: Инстанс текущей страницы
        """
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        return self

    @allure.step("Выполнить авторизацию с логином {username} и паролем {password}")
    def login(self, username: str, password: str) -> 'LoginPage':
        """
        Полный процесс авторизации
        
        Args:
            username (str): Имя пользователя
            password (str): Пароль пользователя
            
        Returns:
            LoginPage: Инстанс текущей страницы
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self