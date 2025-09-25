from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(
             (By.ID, "add-to-cart-sauce-labs-backpack")))
        add_button.click()
        return self

    def add_bolt_t_shirt_to_cart(self):
        add_button = self.driver.find_element(
             By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_button.click()
        return self

    def add_onesie_to_cart(self):
        add_button = self.driver.find_element(
             By.ID, "add-to-cart-sauce-labs-onesie")
        add_button.click()
        return self

    def go_to_cart(self):
        cart_icon = self.driver.find_element(
             By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        self.wait.until(EC.visibility_of_element_located(
             (By.CLASS_NAME, "cart_list")))
        return self

    def get_cart_count(self):
        cart_badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
