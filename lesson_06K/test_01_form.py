import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFormValidation:
    
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Edge()
        yield driver
        driver.quit()
    
    def test_form_validation(self, driver):
        wait = WebDriverWait(driver, 15)
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        # Заполняем форму
        fields_to_fill = [
            ("first-name", "Иван"),
            ("last-name", "Петров"),
            ("address", "Ленина, 55-3"),
            ("e-mail", "test@skypro.com"),
            ("phone", "+79858999887"),
            ("city", "Москва"),
            ("country", "Россия"),
            ("job-position", "QA"),
            ("company", "SkyPro")
        ]
        
        for field_name, value in fields_to_fill:
            field = wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
            field.clear()
            field.send_keys(value)
        
        # Zip code оставляем пустым
        zip_field = driver.find_element(By.NAME, "zip-code")
        zip_field.clear()
        
        # Запоминаем исходные классы полей
        initial_classes = {}
        for field_name in [f[0] for f in fields_to_fill] + ["zip-code"]:
            field = driver.find_element(By.NAME, field_name)
            initial_classes[field_name] = field.get_attribute("class")
        
        # Нажимаем кнопку
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        
        # Ждем изменения классов полей (применения валидации)
        def styles_applied(driver):
            for field_name in initial_classes:
                current_class = driver.find_element(By.NAME, field_name).get_attribute("class")
                if current_class != initial_classes[field_name]:
                    return True
            return False
        
        wait.until(styles_applied)
        
        # Проверяем стили полей
        zip_classes = driver.find_element(By.NAME, "zip-code").get_attribute("class")
        assert any(cls in zip_classes for cls in ["danger", "error", "invalid", "is-invalid"]), \
               f"Zip code должен быть красным. Классы: {zip_classes}"
        
        # Проверяем остальные поля
        for field_name, _ in fields_to_fill:
            field_classes = driver.find_element(By.NAME, field_name).get_attribute("class")
            assert any(cls in field_classes for cls in ["success", "valid", "is-valid"]), \
                   f"Поле {field_name} должно быть зеленым. Классы: {field_classes}"