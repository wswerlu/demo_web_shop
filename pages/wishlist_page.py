from locators import WishlistPageLocators as Locators
from utils.steps import step

from .base_page import BasePage


class WishlistPage(BasePage):
    """
    Методы для работы со страницей корзины.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'wishlist'

    @step('Проверить, что открыта страница вишлиста')
    def should_be_open_wishlist_page(self) -> None:
        """
        Проверка открытия страницы вишлиста.
        """

        self.should_be_open_page_by_path(path=self.path)

    def get_products(self) -> list:
        """
        Получение товаров в вишлисте.
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

    @step('Проверить наличие товаров в вишлисте')
    def should_be_product_in_wishlist(self, product_names: str | list) -> None:
        """
        Проверка наличия товаров в вишлисте.

        :param product_names: наименования товаров, которые должны быть в вишлисте.
        """

        if not isinstance(product_names, list):
            product_names = [product_names]

        product_names_in_cart = [x['name'] for x in self.get_products()]

        for product_name in product_names:
            assert product_name in product_names_in_cart, f'В вишлисте нет товара "{product_name}"'

    @step('Удалить товар "{product_name}" из вишлиста')
    def remove_product_from_wishlist(self, product_name: str) -> None:
        """
        Удаление указанного товара из вишлиста.

        :param product_name: наименование товара, который необходимо удалить из вишлиста.
        """

        with step(f'Активировать чекбокс "Remove" у товара: {product_name}'):
            strategy, locator = Locators.REMOVE_PRODUCT_BY_NAME
            self.find_element(strategy, locator.format(product_name)).click()

        with step('Кликнуть по кнопке "Update wishlist"'):
            self.find_element_clickable(*Locators.UPDATE_WISHLIST_BUTTON).click()

    @step('Проверить, что вишлист пустой')
    def should_be_empty_wishlist(self) -> None:
        """
        Проверка того, что вишлист пустой.
        """

        with step('Проверить отсутствие товаров в корзине'):
            assert self.is_not_element_present(*Locators.PRODUCTS), 'В корзине есть товары'

        with step('Проверить наличие сообщения о том, что корзина пустая'):
            message = self.find_element(*Locators.EMPTY_WISHLIST_MESSAGE).text
            assert message == 'The wishlist is empty!', \
                f'Текущий текст сообщения: {message} не соответствует ожидаемому: The wishlist is empty!'
