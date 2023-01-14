from random import choice

from allure import epic, feature, title

from data.data import PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_WISHLIST


@epic('Frontend')
@feature('Вишлист')
class TestCart:
    """
    Тесты для проверки работы вишлиста
    """

    @title('Добавление товара в вишлист неавторизованным пользователем')
    def test_add_product_to_wishlist_by_unauthorized_user(self, header, product_card_page, wishlist_page,
                                                          notification_bar):
        path = choice(PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_WISHLIST)

        product_card_page.open(path=path)
        product_card_page.should_be_open_product_card_page(path=path)

        product = product_card_page.get_product_data()

        product_card_page.add_product_to_wishlist(is_new_sender=True)
        notification_bar.should_be_message_about_adding_product_to_wishlist()
        notification_bar.close_notification()
        header.can_see_product_quantity_in_wishlist()
        header.open(path=wishlist_page.path)

        wishlist_page.should_be_open_wishlist_page()
        wishlist_page.should_be_product_in_wishlist(product_names=product['name'])

    @title('Удаление товара из вишлиста')
    def test_remove_product_from_wishlist(self, wishlist_page, add_product_to_wishlist_by_unauthorized_user):
        product_name = add_product_to_wishlist_by_unauthorized_user()[0]['name']

        wishlist_page.open(path=wishlist_page.path)
        wishlist_page.should_be_open_wishlist_page()
        wishlist_page.should_be_product_in_wishlist(product_names=product_name)

        wishlist_page.remove_product_from_wishlist(product_name=product_name)
        wishlist_page.should_be_empty_wishlist()

    @title('Переход на страницу вишлиста из хедера')
    def test_go_to_wishlist_page_from_header(self, main_page, header, wishlist_page):
        main_page.open()

        header.go_to_wishlist_page()
        wishlist_page.should_be_open_wishlist_page()
