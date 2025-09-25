from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        return self

    def get_cart_items_count(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)
