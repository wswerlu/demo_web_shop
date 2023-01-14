from random import choice

from allure import epic, feature, title

from data.data import CATEGORIES, PATH_OF_CATEGORIES_WITH_PRODUCTS


@epic('Frontend')
@feature('Каталог')
class TestCatalog:
    """
    Тесты для проверки работы каталога
    """

    @title('Сортировка товаров по алфавиту')
    def test_sort_products_by_alphabet(self, main_page, header, catalog_page, data_catalog_alphabet):
        category_path = choice(PATH_OF_CATEGORIES_WITH_PRODUCTS)

        catalog_page.open(path=category_path)
        catalog_page.should_be_open_catalog_page(path=category_path)

        catalog_page.sort_by(method=data_catalog_alphabet[0])
        catalog_page.should_be_sort_by_alphabet(is_reverse=data_catalog_alphabet[1])

    @title('Сортировка товаров по цене')
    def test_sort_products_by_price(self, main_page, header, catalog_page, data_catalog_price):
        category_path = choice(PATH_OF_CATEGORIES_WITH_PRODUCTS)

        catalog_page.open(path=category_path)
        catalog_page.should_be_open_catalog_page(path=category_path)

        catalog_page.sort_by(method=data_catalog_price[0])
        catalog_page.should_be_sort_by_price(is_reverse=data_catalog_price[1])

    @title('Количество товаров на странице')
    def test_number_of_products_per_page(self, main_page, header, catalog_page, data_catalog_display):
        category_path = choice(PATH_OF_CATEGORIES_WITH_PRODUCTS)

        catalog_page.open(path=category_path)
        catalog_page.should_be_open_catalog_page(path=category_path)

        catalog_page.choose_page_size(page_size=data_catalog_display[0])
        catalog_page.should_be_number_of_products_displayed_per_page(page_size=data_catalog_display[0])

    @title('Переход на страницу каталога из хедера')
    def test_go_to_catalog_page_from_header(self, main_page, header, catalog_page):
        category = choice(CATEGORIES)

        main_page.open()

        header.click_on_category_with_name(category_name=category)
        catalog_page.should_be_open_catalog_page_by_title(expected_title=category)
