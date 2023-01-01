from allure import step

from locators import HeaderLocators as Locators

from .base_page import BasePage


class Header(BasePage):
    """
    Методы для работы с хедером.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Перейти в корзину')
    def go_to_register_page(self) -> None:
        """
        Переход в корзину.
        """

        self.find_element(*Locators.REGISTER_LINK).click()
