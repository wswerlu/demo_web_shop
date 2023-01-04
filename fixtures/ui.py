from random import choice

from pytest import fixture

from data.data import PRODUCTS_WITHOUT_ATTRIBUTES
from pages import (CartPage, CatalogPage, Header, LoginPage, MainPage,
                   ProductCardPage, RegistrationPage, RegistrationSuccessPage)
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

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #


@fixture(scope='function')
def create_user(header, registration_page, main_page):
    """
    Создание пользователя.
    """

    user = UserData()
    firstname = user.firstname()
    lastname = user.lastname()
    email = user.email()
    password = user.password()

    main_page.open()
    header.go_to_register_page()
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
def login_user(header, login_page, main_page, create_user):
    """
    Авторизация пользователя.
    """

    main_page.open()
    header.go_to_login_page()
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
def add_product_to_cart_unauthorized_user(product_card_page):
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
            product_card_page.open(path=choice(PRODUCTS_WITHOUT_ATTRIBUTES))
            product = product_card_page.get_product_data()
            products_list.append(product)

            product_card_page.add_product_to_cart(quantity=product_quantity)
            product_card_page.should_be_message_about_adding_product_to_cart()

        return products_list

    return wrapper
