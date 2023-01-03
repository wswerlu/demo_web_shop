from random import choice

from allure import step

from locators import ProductCardPageLocators as Locators
from utils.generated_test_data import TextData, UserData

from .base_page import BasePage


class ProductCardPage(BasePage):
    """
    Методы для работы со страницей карточки продукта.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Проверить, что открыта страница авторизации')
    def should_be_open_product_card_page(self, path: str) -> None:
        """
        Проверка открытия страницы авторизации.

        :param path: эндпоинт страницы карточки продукта.
        """

        self.should_be_open_page_by_path(path=path)

    @step('Добавить товар в корзину')
    def add_product_to_cart(self, quantity: int = 1) -> None:
        """
        Добавление товара в корзину.

        :param quantity: количество товара, которое необходимо добавить в корзину.
        """

        user = UserData()
        text = TextData()

        if self.is_element_present(*Locators.ATTRIBUTES_BLOCK, timeout=0):

            with step('Заполнить поля c атрибутами товара'):

                attributes = self.find_elements(*Locators.ATTRIBUTES)

                for attribute in attributes:

                    if self.is_element_present_in_element(attribute, *Locators.RADIO_BUTTON, timeout=0):
                        radio_buttons = self.find_elements_in_element(attribute, *Locators.RADIO_BUTTON)
                        choice(radio_buttons).click()

                    elif self.is_element_present_in_element(attribute, *Locators.CHECKBOX, timeout=0):
                        checkboxes = self.find_elements_in_element(attribute, *Locators.CHECKBOX)
                        choice(checkboxes).click()

                    elif self.is_element_present_in_element(attribute, *Locators.SELECT_ELEMENT, timeout=0):
                        self.find_element_in_element(attribute, *Locators.SELECT_ELEMENT).click()
                        options = self.find_elements_in_element(attribute, *Locators.SELECT_OPTION)
                        choice(options).click()

        elif self.is_element_present(*Locators.GIFTCARD_ATTRIBUTES_BLOCK, timeout=0):

            with step('Заполнить данные подарочной карты'):

                recipient_name = self.find_element(*Locators.RECIPIENT_NAME)
                self.send_keys(recipient_name, user.firstname())

                if self.is_element_present(*Locators.RECIPIENT_EMAIL, timeout=0):
                    recipient_email = self.find_element(*Locators.RECIPIENT_EMAIL)
                    self.send_keys(recipient_email, user.email())

                sender_name = self.find_element(*Locators.SENDER_NAME)
                self.send_keys(sender_name, user.firstname())

                if self.is_element_present(*Locators.SENDER_EMAIL, timeout=0):
                    sender_email = self.find_element(*Locators.SENDER_EMAIL)
                    self.send_keys(sender_email, user.email())

                giftcard_message = self.find_element(*Locators.GIFTCARD_MESSAGE)
                self.send_keys(giftcard_message, text.sentence())

        with step('Указать количество товара: {quantity}'):

            quantity_field = self.find_element(*Locators.PRODUCT_QUANTITY)
            self.send_keys(quantity_field, quantity)

        with step('Кликнуть по кнопке "Add to cart"'):

            self.find_element_clickable(*Locators.ADD_TO_CART_BUTTON).click()

    @step('Проверить, что появилось сообщение о добавлении товара в корзину')
    def should_be_message_about_adding_product_to_cart(self) -> None:
        """
        Проверка появления сообщения о добавлении товара в корзину.
        """

        with step('Проверить, что сообщение появилось'):
            assert self.is_element_visible(*Locators.MESSAGE_ABOUT_ADDING_PRODUCT_TO_CART), \
                'Не появилось сообщение о добавлении товара в корзину'

        with step('Проверить текст сообщения'):
            expected_message_text = 'The product has been added to your shopping cart'
            actual_message_text = self.find_visible_element(*Locators.MESSAGE_ABOUT_ADDING_PRODUCT_TO_CART).text.strip()
            assert actual_message_text.strip() == expected_message_text, \
                f'Текущий текст сообщения: {actual_message_text} не соответствует ожидаемому: {expected_message_text}'
