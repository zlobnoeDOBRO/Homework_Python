import allure
from ..pages.login_page import LoginPage
from ..pages.products_page import ProductsPage
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage

@allure.epic("Online Store")
@allure.feature("Полный цикл покупки")
class TestSauceDemo:
    """
    Тесты для полного цикла покупки в интернет-магазине
    """
    
    @allure.id("STORE-1")
    @allure.title("Полный цикл покупки товаров")
    @allure.description("Тест проверяет полный цикл покупки: авторизация, добавление товаров, оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Покупка товаров")
    def test_complete_purchase_flow(self, driver):
        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(driver)
            login_page.open().login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            products_page = ProductsPage(driver)
            products_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
            products_page.add_product_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            products_page.add_product_to_cart("add-to-cart-sauce-labs-onesie")

            cart_count = products_page.get_cart_count()
            assert cart_count == 3, f"Ожидалось 3 товара в корзине, но получено {cart_count}"

        with allure.step("Переход в корзину"):
            products_page.go_to_cart()

        with allure.step("Проверка корзины и переход к оформлению"):
            cart_page = CartPage(driver)
            items_count = cart_page.get_cart_items_count()
            assert items_count == 3, f"Ожидалось 3 товара в корзине, но получено {items_count}"

            cart_page.click_checkout()

        with allure.step("Заполнение информации о покупателе"):
            checkout_page = CheckoutPage(driver)

            checkout_data = {
                "first-name": "John",
                "last-name": "Doe",
                "postal-code": "12345"
            }

            checkout_page.fill_checkout_info(checkout_data)

        with allure.step("Проверка итоговой суммы"):
            total_amount = checkout_page.get_total_price()
            expected_total = 58.29

            assert total_amount == expected_total, f"Ожидалась сумма ${expected_total}, но получено ${total_amount}"