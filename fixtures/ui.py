from random import choice

from pytest import fixture

from data.data import (PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_CART,
                       PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_WISHLIST)
from pages import (CartPage, CatalogPage, CheckoutAsGuestPage,
                   CheckoutCompletedPage, CheckoutPage, Header, LoginPage,
                   MainPage, NotificationBar, ProductCardPage,
                   RegistrationPage, RegistrationSuccessPage, WishlistPage)
from utils.generated_test_data import UserData

# ------------------------------------------------- Фикстуры страниц ------------------------------------------------- #


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)


@fixture(scope='function')
def header(browser):
    return Header(browser)


@fixture(scope='function')
def registration_page(browser):
    return RegistrationPage(browser)


@fixture(scope='function')
def registration_success_page(browser):
    return RegistrationSuccessPage(browser)


@fixture(scope='function')
def login_page(browser):
    return LoginPage(browser)


@fixture(scope='function')
def catalog_page(browser):
    return CatalogPage(browser)


@fixture(scope='function')
def product_card_page(browser):
    return ProductCardPage(browser)


@fixture(scope='function')
def cart_page(browser):
    return CartPage(browser)


@fixture(scope='function')
def checkout_page(browser):
    return CheckoutPage(browser)


@fixture(scope='function')
def checkout_completed_page(browser):
    return CheckoutCompletedPage(browser)


@fixture(scope='function')
def checkout_as_guest_page(browser):
    return CheckoutAsGuestPage(browser)


@fixture(scope='function')
def wishlist_page(browser):
    return WishlistPage(browser)


@fixture(scope='function')
def notification_bar(browser):
    return NotificationBar(browser)

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #


@fixture(scope='function')
def create_user(header, registration_page):
    """
    Создание пользователя.
    """

    user = UserData()
    firstname = user.firstname()
    lastname = user.lastname()
    email = user.email()
    password = user.password()

    registration_page.open(path=registration_page.path)
    registration_page.fill_registration_form(
        is_random=False,
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
    )
    registration_page.click_on_register_button()
    header.logout_user()

    return {
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': password,
    }


@fixture(scope='function')
def login_user(login_page, create_user):
    """
    Авторизация пользователя.
    """

    login_page.open(path=login_page.path)
    login_page.fill_login_form(
        email=create_user['email'],
        password=create_user['password'],
    )
    login_page.click_on_login_button()

    return {
        'firstname': create_user['firstname'],
        'lastname': create_user['lastname'],
        'email': create_user['email'],
        'password': create_user['password'],
    }


@fixture(scope='function')
def add_product_to_cart_by_unauthorized_user(product_card_page, notification_bar):
    """
    Добавление товара в корзину неавторизованным пользователем.
    """

    def wrapper(quantity_of_products: int = 1, product_quantity: int = 1):
        """
        :param quantity_of_products: количество товаров необходимое для теста.
        :param product_quantity: количество 1 товара необходимое для теста.
        """

        products_list = []

        for _ in range(quantity_of_products):
            product_card_page.open(path=choice(PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_CART))
            product = product_card_page.get_product_data()
            products_list.append(product)

            product_card_page.add_product_to_cart(quantity=product_quantity, is_new_sender=True)
            notification_bar.should_be_message_about_adding_product_to_cart()
            notification_bar.close_notification()

        return products_list

    return wrapper


@fixture(scope='function')
def add_product_to_cart_by_authorized_user(product_card_page, notification_bar, login_user):
    """
    Добавление товара в корзину авторизованным пользователем.
    """

    def wrapper(quantity_of_products: int = 1, product_quantity: int = 1):
        """
        :param quantity_of_products: количество товаров необходимое для теста.
        :param product_quantity: количество 1 товара необходимое для теста.
        """

        products_list = []

        for _ in range(quantity_of_products):
            product_card_page.open(path=choice(PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_CART))
            product = product_card_page.get_product_data()
            products_list.append(product)

            product_card_page.add_product_to_cart(quantity=product_quantity)
            notification_bar.should_be_message_about_adding_product_to_cart()
            notification_bar.close_notification()

        return {
            'products': products_list,
            'user': login_user,
        }

    return wrapper


@fixture(scope='function')
def add_product_to_wishlist_by_unauthorized_user(product_card_page, notification_bar):
    """
    Добавление товара в вишлист неавторизованным пользователем.
    """

    def wrapper(quantity_of_products: int = 1, product_quantity: int = 1):
        """
        :param quantity_of_products: количество товаров необходимое для теста.
        :param product_quantity: количество 1 товара необходимое для теста.
        """

        products_list = []

        for _ in range(quantity_of_products):
            product_card_page.open(path=choice(PATH_OF_PRODUCTS_THAT_CAN_BE_ADDED_TO_WISHLIST))
            product = product_card_page.get_product_data()
            products_list.append(product)

            product_card_page.add_product_to_wishlist(quantity=product_quantity, is_new_sender=True)
            notification_bar.should_be_message_about_adding_product_to_wishlist()
            notification_bar.close_notification()

        return products_list

    return wrapper
