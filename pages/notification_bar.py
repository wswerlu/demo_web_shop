from locators import NotificationBarLocators as Locators
from utils.steps import step

from .base_page import BasePage


class NotificationBar(BasePage):
    """
    Методы для работы со страницей каталога.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def should_be_message_about_adding_product(self, expected_message_text: str):
        """
        Проверка появления сообщения о добавлении товара.

        :param expected_message_text: ожидаемый текст сообщения.
        """

        with step('Проверить, что сообщение появилось'):
            assert self.is_element_visible(*Locators.NOTIFICATION_ABOUT_ADDING_PRODUCT), 'Сообщение не появилось'

        with step('Проверить текст сообщения'):
            actual_message_text = self.find_visible_element(*Locators.NOTIFICATION_ABOUT_ADDING_PRODUCT).text.strip()
            assert actual_message_text.strip() == expected_message_text, \
                f'Текущий текст сообщения: {actual_message_text} не соответствует ожидаемому: {expected_message_text}'

    @step('Проверить, что появилось сообщение о добавлении товара в корзину')
    def should_be_message_about_adding_product_to_cart(self) -> None:
        """
        Проверка появления сообщения о добавлении товара в корзину.
        """

        expected_message_text = 'The product has been added to your shopping cart'

        self.should_be_message_about_adding_product(expected_message_text=expected_message_text)

    @step('Проверить, что появилось сообщение о добавлении товара в вишлист')
    def should_be_message_about_adding_product_to_wishlist(self) -> None:
        """
        Проверка появления сообщения о добавлении товара в корзину.
        """

        expected_message_text = 'The product has been added to your wishlist'

        self.should_be_message_about_adding_product(expected_message_text=expected_message_text)
