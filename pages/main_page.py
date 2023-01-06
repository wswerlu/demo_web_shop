from utils.steps import step

from .base_page import BasePage


class MainPage(BasePage):
    """
    Методы для работы со страницей авторизации.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Проверить, что открыта главная страница')
    def should_be_open_main_page(self) -> None:
        """
        Проверка открытия главной страницы.
        """

        self.should_be_open_page_by_path(path='')
