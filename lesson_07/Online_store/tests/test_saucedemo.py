from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    def test_complete_purchase_flow(self, driver):
        # Шаг 1: Авторизация (только создание и использование Page Objects)
        login_page = LoginPage(driver)
        login_page.open().login("standard_user", "secret_sauce")

        # Шаг 2: Добавление товаров в корзину
        products_page = ProductsPage(driver)
        products_page.add_backpack_to_cart()
        products_page.add_bolt_t_shirt_to_cart()
        products_page.add_onesie_to_cart()

        # Проверка количества товаров в корзине (в тесте)
        cart_count = products_page.get_cart_count()
        assert cart_count == 3, f"Expected 3, but got {cart_count}"

        # Переход в корзину
        products_page.go_to_cart()

        # Шаг 3: Проверка корзины и переход к оформлению
        cart_page = CartPage(driver)
        items_count = cart_page.get_cart_items_count()
        assert items_count == 3, f"Expected 3, but got {items_count}"

        cart_page.click_checkout()

        # Шаг 4: Заполнение информации о покупателе
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")

        # Шаг 5: Проверка итоговой суммы
        total_amount = checkout_page.get_total_price()
        expected_total = 58.29

        assert total_amount == expected_total, f"Expected ${expected_total}, \
              got ${total_amount}"
