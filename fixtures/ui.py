from pytest import fixture

from pages import MainPage

# ------------------------------------------------- Фикстуры страниц ------------------------------------------------- #


@fixture(scope='function')
def main_page(browser):
    return MainPage(browser)

# -------------------------------------- Фикстуры для генерации тестовых данных -------------------------------------- #
