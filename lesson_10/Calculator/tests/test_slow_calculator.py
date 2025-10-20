import allure
import sys
import os

# Добавляем путь к корневой папке lesson_10
current_dir = os.path.dirname(os.path.abspath(__file__))
lesson_root = os.path.join(current_dir, '..', '..')
if lesson_root not in sys.path:
    sys.path.insert(0, lesson_root)

# Теперь импортируем через абсолютный путь
from lesson_10.Calculator.pages.slow_calculator_page import SlowCalculatorPage


@allure.epic("Calculator")
@allure.feature("Медленный калькулятор")
class TestSlowCalculator:
    """
    Тесты для функциональности медленного калькулятора
    """
    
    @allure.id("CALC-1")
    @allure.title("Тест калькулятора с задержкой 45 секунд")
    @allure.description("Проверка работы калькулятора с установленной задержкой выполнения операций")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Вычисление с задержкой")
    def test_calculator_with_45_seconds_delay(self, calculator_page):
        """Тест калькулятора с задержкой 45 секунд"""
        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay("45")
        
        with allure.step("Выполнить операцию 7 + 8"):
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")
        
        with allure.step("Ожидать результат 15"):
            calculator_page.wait_for_result("15")
        
        with allure.step("Проверить результат вычислений"):
            result = calculator_page.get_result()
            assert result == "15", f"Ожидался результат 15, но получен {result}"