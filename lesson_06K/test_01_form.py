from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestForm:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_form_validation(self):
        # Открываем страницу
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ждем загрузки формы
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # Заполняем форму значениями
        test_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",  # оставляем пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполняем все поля формы
        for field_name, value in test_data.items():
            if value:  # заполняем только если значение не пустое
                field = self.wait.until(
                    EC.element_to_be_clickable((By.NAME, field_name))
                    )
                field.clear()
                field.send_keys(value)

        # Нажимаем кнопку Submit
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
            )
        submit_button.click()

        # Ждем перехода на новую страницу
        self.wait.until(EC.url_contains("data-types-submitted.html"))

        # Находим все alert элементы на новой странице
        alerts = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".alert")))

        # Проверяем, что поле Zip code подсвечено красным (danger)
        # Четвертый элемент должен быть zip-code
        zip_code_alert = alerts[3]  # четвертый элемент (индекс 3)
        assert "alert-danger" in zip_code_alert.get_attribute("class"), \
            "Zip code поле должно быть подсвечено красным"
        assert zip_code_alert.text == "N/A", \
            "Zip code поле должно содержать текст N/A"

        # Проверяем, что остальные поля подсвечены зеленым (success)
        success_indices = [0, 1, 2, 4, 5, 6, 7, 8, 9]  # индексы успешных полей
        expected_texts = [
            "Иван", "Петров", "Ленина, 55-3", "Москва", "Россия",
            "test@skypro.com", "+7985899998787", "QA", "SkyPro"
        ]

        for i, expected_text in zip(success_indices, expected_texts):
            alert = alerts[i]
            assert "alert-success" in alert.get_attribute("class"), \
                f"Поле с индексом {i} должно быть подсвечено зеленым"
            assert alert.text == expected_text, \
                f"Текст поля с индексом {i} должен быть '{expected_text}'"
