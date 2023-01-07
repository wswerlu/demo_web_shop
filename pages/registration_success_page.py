from locators import RegistrationSuccessPageLocators as Locators
from utils.steps import step

from .base_page import BasePage


class RegistrationSuccessPage(BasePage):
    """
    Методы для работы со страницей подтверждения успешной регистрации.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'registerresult/1'

    @step('Проверить, что открыта страница подтверждения успешной регистрации')
    def should_be_open_registration_success_page(self) -> None:
        """
        Проверка открытия страницы подтверждения успешной регистрации.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Проверить наличие сообщения об успешной регистрации')
    def should_be_confirm_register_message(self) -> None:
        """
        Проверить наличия сообщения об успешной регистрации.
        """

        with step('Проверить наличие сообщения'):
            assert self.is_element_present(*Locators.CONFIRM_MESSAGE)

        with step('Проверить текст сообщения'):
            expected_message_text = 'Your registration completed'
            actual_message_text = self.find_element(*Locators.CONFIRM_MESSAGE).text
            assert expected_message_text == actual_message_text, \
                f'Текущий текст сообщения: {actual_message_text} не соответствует ожидаемому: {expected_message_text}'
