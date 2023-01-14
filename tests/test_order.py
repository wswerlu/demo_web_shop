from allure import epic, feature, title


@epic('Frontend')
@feature('Заказ')
class TestOrder:
    """
    Тесты для проверки заказов
    """

    @title('Создание заказа c доставкой авторизованным пользователем, у которого в профиле не указан адрес')
    def test_create_order_with_delivery_by_authorized_user_without_address(self, cart_page, checkout_page,
                                                                           checkout_completed_page,
                                                                           add_product_to_cart_by_authorized_user):
        product_name = add_product_to_cart_by_authorized_user()['products'][0]['name']

        cart_page.open(path=cart_page.path)
        cart_page.should_be_open_cart_page()
        cart_page.should_be_product_in_cart(product_names=product_name)

        cart_page.agree_to_terms_of_service()
        cart_page.click_on_checkout_button()
        checkout_page.should_be_open_checkout_page()

        checkout_page.fill_billing_address_form()
        checkout_page.fill_shipping_address_form()
        checkout_page.choose_shipping_method()
        checkout_page.choose_payment_method()
        checkout_page.fill_payment_information()
        checkout_page.confirm_order()

        checkout_completed_page.should_be_open_checkout_completed_page()
        checkout_completed_page.can_see_message_about_successfully_creating_order()

    @title('Создание заказа c самовывозом неавторизованным пользователем')
    def test_create_order_with_pick_up_by_guest(self, cart_page, checkout_as_guest_page, checkout_page,
                                                checkout_completed_page, add_product_to_cart_by_unauthorized_user):
        product_name = add_product_to_cart_by_unauthorized_user()[0]['name']

        cart_page.open(path=cart_page.path)
        cart_page.should_be_open_cart_page()
        cart_page.should_be_product_in_cart(product_names=product_name)

        cart_page.agree_to_terms_of_service()
        cart_page.click_on_checkout_button()
        checkout_as_guest_page.should_be_open_checkout_as_guest_page()

        checkout_as_guest_page.click_on_checkout_as_guest_button()
        checkout_page.should_be_open_checkout_page()

        checkout_page.fill_billing_address_form(is_new_user=True)
        checkout_page.fill_shipping_address_form(is_pick_up=True)
        checkout_page.choose_payment_method()
        checkout_page.fill_payment_information()
        checkout_page.confirm_order()

        checkout_completed_page.should_be_open_checkout_completed_page()
        checkout_completed_page.can_see_message_about_successfully_creating_order()
