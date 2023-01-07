from allure import epic, feature, title


@epic('Frontend')
@feature('Каталог')
class TestCatalog:
    """
    Тесты для проверки работы каталога
    """

    @title('Сортировка товаров по алфавиту')
    def test_sort_products_by_alphabet(self, main_page, header, catalog_page, data_catalog_alphabet):
        main_page.open()
        main_page.should_be_open_main_page()

        category_name = header.click_on_random_category_and_get_its_name()
        catalog_page.should_be_open_catalog_page_by_title(category_name=category_name)

        catalog_page.sort_by(method=data_catalog_alphabet[0])
        catalog_page.should_be_sort_by_alphabet(is_reverse=data_catalog_alphabet[1])
