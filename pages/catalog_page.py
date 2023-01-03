from re import sub

from allure import step

from locators import CatalogPageLocators as Locators

from .base_page import BasePage


class CatalogPage(BasePage):
    """
    Методы для работы со страницей каталога.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Проверить, что открыта страница каталога: {category_name}')
    def should_be_open_catalog_page_by_title(self, category_name: str) -> None:
        """
        Проверка открытия указанной страницы каталога.
        """

        actual_title = self.find_element(*Locators.TITLE).text

        if '&' in category_name or 'GIFT' in category_name:
            expected_title = category_name.title()
        else:
            expected_title = category_name.capitalize()

        assert actual_title == expected_title, \
            f'Текущий заголовок страницы: {actual_title} не соответствует ожидаемому: {expected_title}'

    def get_products(self) -> list:
        """
        Получение товаров со страницы каталога.
        """

        products = self.find_elements(*Locators.PRODUCTS)

        products_list = []

        for product in products:
            _id = self.find_element_in_element(product, *Locators.PRODUCT_ID).get_attribute('data-productid')

            url = self.find_element_in_element(product, *Locators.PRODUCT_NAME).get_attribute('href')
            path = sub(self.base_url, '', url)

            name = self.find_element_in_element(product, *Locators.PRODUCT_NAME).text

            if self.is_element_present_in_element(product, *Locators.PRODUCT_OLD_PRICE):
                old_price = self.find_element_in_element(product, *Locators.PRODUCT_OLD_PRICE).text
            else:
                old_price = None

            actual_price_string = self.find_element_in_element(product, *Locators.PRODUCT_ACTUAL_PRICE).text
            if 'From' in actual_price_string:
                actual_price = sub(r'From ', '', actual_price_string)
            else:
                actual_price = actual_price_string

            is_available = self.is_element_present_in_element(product, *Locators.ADD_TO_CART_BUTTON)

            products_list.append(
                {
                    'id': int(_id),
                    'path': path,
                    'name': name,
                    'old_price': float(old_price) if old_price else None,
                    'actual_price': float(actual_price),
                    'is_available': is_available,
                },
            )

        return products_list

    def get_available_products(self) -> list:
        """
        Получение доступных для заказа товаров со страницы каталога.
        """

        products = self.get_products()

        available_products = [x for x in products if x['is_available'] is True]

        if not len(available_products):
            raise AssertionError('Нет доступных товаров для заказа')

        return available_products

    @step('Перейти на страницу карточки товара c id: {product_id}')
    def go_to_product_card_page(self, product_id: str) -> None:
        """
        Переход на страницу карточки указанного товара.

        :param product_id: id товара.
        """

        strategy, locator = Locators.GO_TO_PRODUCT_CARD_BY_ID

        product = self.find_element(strategy, locator.format(product_id))
        product.click()
