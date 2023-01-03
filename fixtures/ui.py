from pytest import fixture

from pages import (Header, LoginPage, MainPage, RegistrationPage,
                   RegistrationSuccessPage)
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

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #


@fixture(scope='function')
def create_user(header, registration_page, main_page):
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
