from allure import step

from locators import CartPageLocators as Locators

from .base_page import BasePage


class CartPage(BasePage):
    """
    Методы для работы со страницей корзины.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'cart'

    @step('Проверить, что открыта страница корзины')
    def should_be_open_cart_page(self) -> None:
        """
        Проверка открытия страницы корзины.
        """

        self.should_be_open_page_by_path(path=self.path)

    def get_products(self) -> list:
        """
        Получение товаров в корзине.
        """

        products = self.find_elements(*Locators.PRODUCTS)

        products_list = []

        for product in products:

            name = self.find_element_in_element(product, *Locators.PRODUCT_NAME).text
            price = self.find_element_in_element(product, *Locators.PRODUCT_PRICE).text
            quantity = self.find_element_in_element(product, *Locators.PRODUCT_QUANTITY).get_attribute('value')
            total_price = self.is_element_present_in_element(product, *Locators.PRODUCT_TOTAL_PRICE)

            products_list.append(
                {
                    'name': name,
                    'price': float(price),
                    'quantity': int(quantity),
                    'total_price': total_price,
                },
            )

        return products_list

    @step('Проверить наличие товаров в корзине')
    def should_be_product_in_cart(self, product_names: str | list) -> None:
        """
        Проверка наличия товаров в корзине.

        :param product_names: наименования товаров, которые должны быть в корзине.
        """

        if not isinstance(product_names, list):
            product_names = [product_names]

        product_names_in_cart = [x['name'] for x in self.get_products()]

        for product_name in product_names:
            assert product_name in product_names_in_cart, f'В корзине нет товара "{product_name}"'
