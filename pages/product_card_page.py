from random import choice, randint

from locators import ProductCardPageLocators as Locators
from utils.generated_test_data import TextData, UserData
from utils.steps import step

from .base_page import BasePage


class ProductCardPage(BasePage):
    """
    Методы для работы со страницей карточки продукта.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Проверить, что открыта страница карточки продукта с эндпоинтом: {path}')
    def should_be_open_product_card_page(self, path: str) -> None:
        """
        Проверка открытия страницы карточки продукта.

        :param path: эндпоинт страницы карточки продукта.
        """

        self.should_be_open_page_by_path(path=path)

    @step('Добавить товар в корзину')
    def add_product_to_cart(self, quantity: int = 1, is_new_sender: bool = False) -> None:
        """
        Добавление товара в корзину.

        :param quantity: количество товара, которое необходимо добавить в корзину.
        :param is_new_sender: True — необходимо заполнить поля "Your name",
         "Your email", False — эти поля заполнять не нужно
          (параметр актуален при добавлении в корзину подарочной карты).
        """

        if self.is_element_present(*Locators.ATTRIBUTES_BLOCK, timeout=0):

            self.fill_attributes_block()

        elif self.is_element_present(*Locators.GIFTCARD_ATTRIBUTES_BLOCK, timeout=0):

            self.fill_gift_card_form(is_new_sender=is_new_sender)

        with step(f'Указать количество товара: {quantity}'):

            quantity_field = self.find_element(*Locators.PRODUCT_QUANTITY)
            self.send_keys(quantity_field, quantity)

        with step('Кликнуть по кнопке "Add to cart"'):

            self.find_element_clickable(*Locators.ADD_TO_CART_BUTTON).click()

    @step('Заполнить поля c атрибутами товара')
    def fill_attributes_block(self):
        """
        Заполнение полей с атрибутами товара.
        """

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

            elif self.is_element_present_in_element(attribute, *Locators.TEXT_FIELD, timeout=0):
                text_field = self.find_element_in_element(attribute, *Locators.TEXT_FIELD)
                self.send_keys(text_field, randint(1, 10))

    @step('Заполнить данные подарочной карты')
    def fill_gift_card_form(self, is_new_sender: bool = False):
        """
        Заполнение данных подарочной карты.

        :param is_new_sender: True — необходимо заполнить поля "Your name",
         "Your email", False — эти поля заполнять не нужно.
        """

        user = UserData()
        text = TextData()

        recipient_name = self.find_element(*Locators.RECIPIENT_NAME)
        self.send_keys(recipient_name, user.firstname())

        if self.is_element_present(*Locators.RECIPIENT_EMAIL, timeout=0):
            recipient_email = self.find_element(*Locators.RECIPIENT_EMAIL)
            self.send_keys(recipient_email, user.email())

        if is_new_sender:
            sender_name = self.find_element(*Locators.SENDER_NAME)
            self.send_keys(sender_name, user.firstname())

            if self.is_element_present(*Locators.SENDER_EMAIL, timeout=0):
                sender_email = self.find_element(*Locators.SENDER_EMAIL)
                self.send_keys(sender_email, user.email())

        gift_card_message = self.find_element(*Locators.GIFTCARD_MESSAGE)
        self.send_keys(gift_card_message, text.sentence())

    def get_product_data(self) -> dict:
        """
        Получение данных по товару.
        """

        _id = self.find_element(*Locators.PRODUCT_QUANTITY).get_attribute('value')
        name = self.find_element(*Locators.PRODUCT_NAME).text
        short_description = self.find_element(*Locators.PRODUCT_NAME).text
        full_description = self.find_element(*Locators.PRODUCT_NAME).text
        price = self.find_element(*Locators.PRODUCT_PRICE).text

        if self.is_element_present(*Locators.PRODUCT_OLD_PRICE):
            old_price = self.find_element(*Locators.PRODUCT_OLD_PRICE).text
        else:
            old_price = None

        return {
            'id': _id,
            'name': name,
            'short_description': short_description,
            'full_description': full_description,
            'old_price': float(old_price) if old_price else None,
            'price': float(price),
        }

    @step('Добавить товар в вишлист')
    def add_product_to_wishlist(self, quantity: int = 1, is_new_sender: bool = False) -> None:
        """
        Добавление товара в вишлист.

        :param quantity: количество товара, которое необходимо добавить в вишлист.
        :param is_new_sender: True — необходимо заполнить поля "Your name",
         "Your email", False — эти поля заполнять не нужно
          (параметр актуален при добавлении в вишлист подарочной карты).
        """

        if self.is_element_present(*Locators.ATTRIBUTES_BLOCK, timeout=0):

            self.fill_attributes_block()

        elif self.is_element_present(*Locators.GIFTCARD_ATTRIBUTES_BLOCK, timeout=0):

            self.fill_gift_card_form(is_new_sender=is_new_sender)

        with step(f'Указать количество товара: {quantity}'):

            quantity_field = self.find_element(*Locators.PRODUCT_QUANTITY)
            self.send_keys(quantity_field, quantity)

        with step('Кликнуть по кнопке "Add to wishlist"'):

            self.find_element_clickable(*Locators.ADD_TO_CART_WISHLIST).click()
