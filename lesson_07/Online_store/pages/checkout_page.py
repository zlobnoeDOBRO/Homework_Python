from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        first_name_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name")))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        return self

    def enter_zip_code(self, zip_code):
        zip_code_field = self.driver.find_element(By.ID, "postal-code")
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)
        return self

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")))
        return self

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()
        return self

    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return float(total_amount)

    def finish_checkout(self):
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        return self
