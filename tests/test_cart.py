from random import choice

from allure import epic, feature, title


@epic('Frontend')
@feature('Корзина')
class TestCart:
    """
    Тесты для проверки работы корзины
    """

    @title('Добавление товара в корзину из карточки заказа авторизованным пользователем')
    def test_add_product_to_cart_from_product_card_by_authorized_user(self, main_page, header, catalog_page,
                                                                      product_card_page, cart_page, login_user):
        main_page.open()
        main_page.should_be_open_main_page()

        category_name = header.click_on_random_category_and_get_its_name()
        catalog_page.should_be_open_catalog_page_by_title(category_name=category_name)

        product = choice(catalog_page.get_available_products())
        catalog_page.go_to_product_card_page(product_id=product['id'])
        product_card_page.should_be_open_product_card_page(path=product['path'])

        product_card_page.add_product_to_cart()
        product_card_page.should_be_message_about_adding_product_to_cart()
        header.can_see_product_quantity_in_cart()
        header.go_to_cart_page()

        cart_page.should_be_open_cart_page()
        cart_page.should_be_product_in_cart(product_names=product['name'])
