from pytest import fixture

from pages import Header, MainPage, RegistrationPage, RegistrationSuccessPage

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

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #
