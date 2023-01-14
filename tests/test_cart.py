from random import choice

from allure import epic, feature, title

from data.data import PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_CART


@epic('Frontend')
@feature('Корзина')
class TestCart:
    """
    Тесты для проверки работы корзины
    """

    @title('Добавление товара в корзину из карточки заказа авторизованным пользователем')
    def test_add_product_to_cart_from_product_card_by_authorized_user(self, header, product_card_page, cart_page,
                                                                      notification_bar, login_user):
        product_path = choice(PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_CART)

        product_card_page.open(path=product_path)
        product_card_page.should_be_open_product_card_page(path=product_path)
        product = product_card_page.get_product_data()

        product_card_page.add_product_to_cart()
        notification_bar.should_be_message_about_adding_product_to_cart()
        notification_bar.close_notification()
        header.can_see_product_quantity_in_cart()
        header.open(path=cart_page.path)

        cart_page.should_be_open_cart_page()
        cart_page.should_be_product_in_cart(product_names=product['name'])

    @title('Товар отображается во всплывающей корзине')
    def test_product_in_flyout_cart(self, main_page, header, add_product_to_cart_by_unauthorized_user):
        product_name = add_product_to_cart_by_unauthorized_user()[0]['name']

        header.can_see_product_in_flyout_cart(product_names=product_name)

    @title('Удаление товара из корзины')
    def test_remove_product_from_cart(self, main_page, header, cart_page, add_product_to_cart_by_unauthorized_user):
        product_name = add_product_to_cart_by_unauthorized_user()[0]['name']

        cart_page.open(path=cart_page.path)
        cart_page.should_be_open_cart_page()
        cart_page.should_be_product_in_cart(product_names=product_name)

        cart_page.remove_product_from_cart(product_name=product_name)
        cart_page.should_be_empty_cart()

    @title('Добавление товара в корзину из вишлиста')
    def test_add_product_to_cart_from_wishlist(self, header, cart_page, wishlist_page,
                                               add_product_to_wishlist_by_unauthorized_user):
        product_name = add_product_to_wishlist_by_unauthorized_user()[0]['name']

        wishlist_page.open(path=wishlist_page.path)
        wishlist_page.should_be_open_wishlist_page()
        wishlist_page.should_be_product_in_wishlist(product_names=product_name)

        wishlist_page.add_product_to_cart(product_name=product_name)
        cart_page.should_be_open_cart_page()

        header.can_see_product_quantity_in_wishlist(expected_quantity=0)
        cart_page.should_be_product_in_cart(product_names=product_name)

    @title('Переход на страницу корзины из хедера')
    def test_go_to_login_page_from_header(self, main_page, header, cart_page):
        main_page.open()

        header.go_to_cart_page()
        cart_page.should_be_open_cart_page()
