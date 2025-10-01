class TestSlowCalculator:
    def test_calculator_with_45_seconds_delay(self, calculator_page):
        """Тест калькулятора с задержкой 45 секунд"""
        calculator_page.set_delay("45")
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        calculator_page.wait_for_result("15")
        result = calculator_page.get_result()
        assert result == "15"
