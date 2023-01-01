from pytest import fixture

from pages import Header, MainPage

# ------------------------------------------------- Фикстуры страниц ------------------------------------------------- #


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)


@fixture(scope='function')
def header(browser):
    return Header(browser)

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #
