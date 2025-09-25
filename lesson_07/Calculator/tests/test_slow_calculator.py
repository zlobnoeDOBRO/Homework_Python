from selenium import webdriver
from pages.slow_calculator_page import SlowCalculatorPage


def test_calculator_shows_15_after_45_seconds():
    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)

    page.open()
    page.set_delay("45")
    page.press_seven()
    page.press_plus()
    page.press_eight()
    page.press_equals()

    result = page.get_result()
    assert result == "15"

    driver.quit()
