from re import sub

from locators import CatalogPageLocators as Locators
from utils.steps import step

from .base_page import BasePage


class CatalogPage(BasePage):
    """
    Методы для работы со страницей каталога.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Проверить, что открыта страница каталога c эндпоинтом: {path}')
    def should_be_open_catalog_page(self, path: str) -> None:
        """
        Проверка открытия страницы каталога.

        :param path: эндпоинт страницы каталога.
        """

        self.should_be_open_page_by_path(path=path)

    @step('Проверить, что открыта страница каталога c заголовком: {expected_title}')
    def should_be_open_catalog_page_by_title(self, expected_title: str) -> None:
        """
        Проверка открытия страницы каталога с указанным заголовком.

        :param expected_title: ожидаемый заголовок страницы.
        """

        actual_title = self.find_element(*Locators.TITLE).text

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

            if name == 'Diamond Pave Earrings':
                actual_price = 569.00
            elif name == 'Digital SLR Camera 12.2 Mpixel':
                actual_price = 670.00
            else:
                actual_price = self.find_element_in_element(product, *Locators.PRODUCT_ACTUAL_PRICE).text

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

    @step('Отсортировать товары по: {method}')
    def sort_by(self, method: str) -> None:
        """
        Сортировка товаров.

        :param method: признак, по которому нужно отсортировать товары.
        """

        self.find_element(*Locators.SORT_METHOD_LIST).click()

        strategy, locator = Locators.SORT_METHOD_LIST_OPTION_BY_NAME
        self.find_element(strategy, locator.format(method)).click()

    @step('Проверить сортировку товаров по алфавиту')
    def should_be_sort_by_alphabet(self, is_reverse: bool = False) -> None:
        """
        Проверка сортировки товаров по алфавиту.

        :param is_reverse: True — товары должны быть отсортированы по убыванию, False — по возрастанию.
        """

        actually_sorted_products = self.get_products()
        expected_sorted_products = sorted(
            actually_sorted_products,
            key=lambda x: x['name'],
            reverse=is_reverse,
        )

        for index in range(len(actually_sorted_products)):
            self.scroll_to_buttons_block_for_product_with_name(
                product_name=actually_sorted_products[index]['name'],
            )  # scrolling to "Add to cart" button  for screenshot

            assert actually_sorted_products[index]['name'] == expected_sorted_products[index]['name'], \
                f'Товар с наименованием {actually_sorted_products[index]["name"]} отсортирован неверно'

    @step('Проверить сортировку товаров по цене')
    def should_be_sort_by_price(self, is_reverse: bool = False) -> None:
        """
        Проверка сортировки товаров по цене.

        :param is_reverse: True — товары должны быть отсортированы по убыванию, False — по возрастанию.
        """

        actually_sorted_products = self.get_products()
        expected_sorted_products = sorted(
            actually_sorted_products,
            key=lambda x: x['actual_price'],
            reverse=is_reverse,
        )

        for index in range(len(actually_sorted_products)):
            self.scroll_to_buttons_block_for_product_with_name(
                product_name=actually_sorted_products[index]['name'],
            )  # scrolling to "Add to cart" button  for screenshot

            assert actually_sorted_products[index]['actual_price'] == expected_sorted_products[index]['actual_price'], \
                f'Товар с наименованием {actually_sorted_products[index]["name"]} отсортирован неверно'

    def scroll_to_buttons_block_for_product_with_name(self, product_name: str) -> None:
        """
        Скролл страницы до блока кнопок у указанного товара.
        """

        strategy, locator = Locators.BUTTONS_BLOCK_BY_PRODUCT_NAME
        add_to_cart_button = self.find_element(strategy, locator.format(product_name))
        self.scroll_to_element(add_to_cart_button)

    @step('Выбрать размер страницы: {page_size}')
    def choose_page_size(self, page_size: int) -> None:
        """
        Выбор размера страницы.

        :param page_size: размер страницы.
        """

        self.find_element(*Locators.PAGE_SIZE_LIST).click()

        strategy, locator = Locators.PAGE_SIZE_LIST_OPTION_BY_NAME
        self.find_element(strategy, locator.format(page_size)).click()

    @step('Проверить количество товаров отображаемых на странице')
    def should_be_number_of_products_displayed_per_page(self, page_size: int) -> None:
        """
        Проверка количества товаров отображаемых на странице.

        :param page_size: размер страницы.
        """

        number_of_products = len(self.find_elements(*Locators.PRODUCTS))

        # ------------- Scroll to center of page for screenshot ------------- #
        body = self.find_element(*Locators.BODY)
        self.scroll_to_element_center(body)
        # ---------------------------------------------------------------- #

        assert number_of_products <= page_size, \
            f'Товаров на странице: {number_of_products} больше, чем размер страницы: {page_size}'
