from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    delay_input = (By.ID, "delay")
    screen = (By.CSS_SELECTOR, "#calculator .screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get("https://bonigarcia.dev/" +
                        "selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value: str):
        delay_elem = self.driver.find_element(*self.delay_input)
        delay_elem.clear()
        delay_elem.send_keys(value)

    def press_seven(self):
        self._click_button("7")

    def press_eight(self):
        self._click_button("8")

    def press_plus(self):
        self._click_button("+")

    def press_equals(self):
        self._click_button("=")

    def get_result(self) -> str:
        # Ждём, пока на экране не появится "15"
        self.wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text

    def _click_button(self, label: str):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']")
        button.click()
