from datetime import datetime
from random import choice, randrange

from allure import step

from data.data import CREDIT_CARD_TYPE
from locators import CheckoutPageLocators as Locators
from utils.generated_test_data import AddressData, PaymentData, UserData

from .base_page import BasePage


class CheckoutPage(BasePage):
    """
    Методы для работы со страницей создания заказа.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'onepagecheckout'
    user = UserData()
    address = AddressData()

    @step('Проверить, что открыта страница создания заказа')
    def should_be_open_checkout_page(self) -> None:
        """
        Проверка открытия страницы создания заказа.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Заполнить форму адреса выставления счета')
    def fill_billing_address_form(self, country: str | None = None, state: str | None = None, city: str | None = None,
                                  full_address: str | None = None, zip_code: str | None = None,
                                  phone: str | None = None, is_random: bool = True, is_new_user: bool = False,
                                  firstname: str | None = None, lastname: str | None = None,
                                  email: str | None = None) -> None:
        """
        Заполнение формы адреса выставления счета указанными данными.

        :param country: страна.
        :param state: штат (указывать, если страна United State или Canada).
        :param city: город.
        :param full_address: адрес.
        :param zip_code: почтовый индекс.
        :param phone: телефон пользователя.
        :param is_random: True — нужны произвольные данные (остальные параметры указывать не надо,
         в этом случае страной по умолчанию будет: Russia), False — нужны конкретные данные.
        :param is_new_user: True — нужно заполнить поля: "First name", "Last name", "Email",
         False — не нужно заполнять эти поля.
        :param firstname: имя.
        :param lastname: фамилия.
        :param email: email.
        """

        if is_random:
            country = 'Russia'
            city = self.address.city()
            full_address = self.address.full_address()
            zip_code = self.address.postal_code()
            phone = self.user.phone()

            if is_new_user:
                firstname = self.user.firstname()
                lastname = self.user.lastname()
                email = self.user.email()

        if is_new_user:
            with step(f'Заполнить поле "First name" значением: {firstname}'):
                firstname_field = self.find_element(*Locators.BILLING_FIRSTNAME)
                self.send_keys(field=firstname_field, value=firstname)

            with step(f'Заполнить поле "Last name" значением: {lastname}'):
                lastname_field = self.find_element(*Locators.BILLING_LASTNAME)
                self.send_keys(field=lastname_field, value=lastname)

            with step(f'Заполнить поле "Email" значением: {email}'):
                email_field = self.find_element(*Locators.BILLING_EMAIL)
                self.send_keys(field=email_field, value=email)

        with step(f'Выбрать страну: {country}'):
            self.find_element(*Locators.BILLING_COUNTRY_LIST).click()

            strategy, locator = Locators.BILLING_COUNTRY_LIST_OPTION_BY_NAME
            self.find_element(strategy, locator.format(country)).click()

        if state:
            with step(f'Выбрать штат: {state}'):
                self.find_element(*Locators.BILLING_STATE_LIST).click()

                strategy, locator = Locators.BILLING_STATE_LIST_OPTION_BY_NAME
                self.find_element(strategy, locator.format(country)).click()

        with step(f'Заполнить поле "City" значением: {city}'):
            city_field = self.find_element(*Locators.BILLING_CITY)
            self.send_keys(field=city_field, value=city)

        with step(f'Заполнить поле "Address 1" значением: {full_address}'):
            address_field = self.find_element(*Locators.BILLING_ADDRESS)
            self.send_keys(field=address_field, value=full_address)

        with step(f'Заполнить поле "Zip / postal code" значением: {zip_code}'):
            zip_code_field = self.find_element(*Locators.BILLING_ZIP_CODE)
            self.send_keys(field=zip_code_field, value=zip_code)

        with step(f'Заполнить поле "Phone number" значением: {phone}'):
            phone_field = self.find_element(*Locators.BILLING_PHONE)
            self.send_keys(field=phone_field, value=phone)

        with step('Кликнуть по кнопке "Continue"'):
            self.find_element_clickable(*Locators.BILLING_CONTINUE_BUTTON).click()

    @step('Заполнить форму адреса доставки')
    def fill_shipping_address_form(self, is_billing_address: bool = True, is_pick_up: bool = False,
                                   country: str | None = None, state: str | None = None, city: str | None = None,
                                   full_address: str | None = None, zip_code: str | None = None,
                                   phone: str | None = None, is_random: bool = True, is_new_user: bool = False,
                                   firstname: str | None = None, lastname: str | None = None,
                                   email: str | None = None) -> None:
        """
        Заполнение формы адреса доставки указанными данными.

        :param is_billing_address: True — адрес доставки совпадает с адресом выставления счета,
         False — адрес доставки не совпадает с адресом выставления счета.
        :param is_pick_up: True — не нужна доставка, False — нужна доставка.
        :param country: страна.
        :param state: штат (указывать, если страна United State или Canada).
        :param city: город.
        :param full_address: адрес.
        :param zip_code: почтовый индекс.
        :param phone: телефон пользователя.
        :param is_random: True — нужны произвольные данные (остальные параметры указывать не надо,
         в этом случае страной по умолчанию будет: Russia), False — нужны конкретные данные.
        :param is_new_user: True — нужно заполнить поля: "First name", "Last name", "Email",
         False — не нужно заполнять эти поля.
        :param firstname: имя.
        :param lastname: фамилия.
        :param email: email.
        """

        if self.is_element_present(*Locators.STEP_SHIPPING, timeout=0):
            if is_pick_up:
                with step('Выбрать самовывоз из магазина'):
                    self.find_element(*Locators.PICK_UP_IN_STORE_CHECKBOX).click()
            else:
                if not is_billing_address:
                    if is_random:
                        country = 'Russia'
                        city = self.address.city()
                        full_address = self.address.full_address()
                        zip_code = self.address.postal_code()
                        phone = self.user.phone()

                        if is_new_user:
                            firstname = self.user.firstname()
                            lastname = self.user.lastname()
                            email = self.user.email()

                    with step('Выбрать адрес: New address'):
                        self.find_element(*Locators.SHIPPING_ADDRESS_LIST).click()

                        strategy, locator = Locators.SHIPPING_ADDRESS_LIST_OPTION_BY_NAME
                        self.find_element(strategy, locator.format('New Address')).click()

                    if is_new_user:
                        with step(f'Заполнить поле "First name" значением: {firstname}'):
                            firstname_field = self.find_element(*Locators.SHIPPING_FIRSTNAME)
                            self.send_keys(field=firstname_field, value=firstname)

                        with step(f'Заполнить поле "Last name" значением: {lastname}'):
                            lastname_field = self.find_element(*Locators.SHIPPING_LASTNAME)
                            self.send_keys(field=lastname_field, value=lastname)

                        with step(f'Заполнить поле "Email" значением: {email}'):
                            email_field = self.find_element(*Locators.SHIPPING_EMAIL)
                            self.send_keys(field=email_field, value=email)

                    with step(f'Выбрать страну: {country}'):
                        self.find_element(*Locators.SHIPPING_COUNTRY_LIST).click()

                        strategy, locator = Locators.SHIPPING_COUNTRY_LIST_OPTION_BY_NAME
                        self.find_element(strategy, locator.format(country)).click()

                    if state:
                        with step(f'Выбрать штат: {state}'):
                            self.find_element(*Locators.SHIPPING_STATE_LIST).click()

                            strategy, locator = Locators.SHIPPING_STATE_LIST_OPTION_BY_NAME
                            self.find_element(strategy, locator.format(country)).click()

                    with step(f'Заполнить поле "City" значением: {city}'):
                        city_field = self.find_element(*Locators.SHIPPING_CITY)
                        self.send_keys(field=city_field, value=city)

                    with step(f'Заполнить поле "Address 1" значением: {full_address}'):
                        address_field = self.find_element(*Locators.SHIPPING_ADDRESS)
                        self.send_keys(field=address_field, value=full_address)

                    with step(f'Заполнить поле "Zip / postal code" значением: {zip_code}'):
                        zip_code_field = self.find_element(*Locators.SHIPPING_ZIP_CODE)
                        self.send_keys(field=zip_code_field, value=zip_code)

                    with step(f'Заполнить поле "Phone number" значением: {phone}'):
                        phone_field = self.find_element(*Locators.SHIPPING_PHONE)
                        self.send_keys(field=phone_field, value=phone)

            with step('Кликнуть по кнопке "Continue"'):
                self.find_element_clickable(*Locators.SHIPPING_CONTINUE_BUTTON).click()

    @step('Выбрать способ доставки')
    def choose_shipping_method(self, shipping_method: str = 'Ground') -> None:
        """
        Выбрать способ доставки.

        :param shipping_method: способ доставки.
         Допустимые значения: Ground, Next Day Air, 2nd Day Air (по умолчанию Ground).
        """

        if self.is_element_present(*Locators.STEP_SHIPPING_METHOD, timeout=0):
            with step(f'Выбрать способ доставки: {shipping_method}'):
                strategy, locator = Locators.SHIPPING_METHOD_RADIO_BUTTON_BY_NAME
                self.find_element(strategy, locator.format(shipping_method)).click()

            with step('Кликнуть по кнопке "Continue"'):
                self.find_element_clickable(*Locators.SHIPPING_METHOD_CONTINUE_BUTTON).click()

    @step('Выбрать способ оплаты')
    def choose_payment_method(self, payment_method: str = 'Cash On Delivery (COD)') -> None:
        """
        Выбрать способ оплаты.

        :param payment_method: способ оплаты.
         Допустимые значения: Cash On Delivery (COD), Check / Money Order, Credit Card, Purchase Order
          (по умолчанию Cash On Delivery (COD)).
        """

        with step(f'Выбрать способ оплаты: {payment_method}'):
            strategy, locator = Locators.PAYMENT_METHOD_RADIO_BUTTON_BY_NAME
            self.find_element(strategy, locator.format(payment_method)).click()

        with step('Кликнуть по кнопке "Continue"'):
            self.find_element_clickable(*Locators.PAYMENT_METHOD_CONTINUE_BUTTON).click()

    @step('Заполнить информацию по оплате')
    def fill_payment_information(self, payment_method: str | None = None, card_type: str | None = None,
                                 cardholder_name: str | None = None, card_number: str | None = None,
                                 card_expiration_month: str | None = None, card_expiration_year: str | None = None,
                                 card_code: str | None = None, purchase_order_number: str | None = None,
                                 is_random: bool = True) -> None:
        """
        Заполнение информации по оплате.

        :param payment_method: способ оплаты. Допустимые значения: Credit Card, Purchase Order.
        :param card_type: тип карты. Допустимые значения: Visa, Master card, Amex, Discover.
        :param cardholder_name: имя держателя карты.
        :param card_number: номер карты.
        :param card_expiration_month: месяц окончания действия карты.
        :param card_expiration_year: год окончания действия карты.
        :param card_code: CVV код.
        :param purchase_order_number: номер заказа на закупку.
        :param is_random: True — нужны произвольные данные, False — нужны конкретные данные.
        """

        if payment_method == 'Credit Card':
            if is_random:
                payment = PaymentData()
                card_type = choice(list(CREDIT_CARD_TYPE.keys()))
                cardholder_name = payment.cardholder_name()
                card_number = payment.card_number(card_type=card_type)
                card_expiration_month = f'{randrange(1, 13):02d}'
                card_expiration_year = randrange(datetime.now().year, 2038)
                card_code = payment.card_code()

            with step(f'Выбрать тип карты: {card_type}'):
                self.find_element(*Locators.CARD_TYPE_LIST).click()

                strategy, locator = Locators.CARD_TYPE_LIST_OPTION_BY_NAME
                self.find_element(strategy, locator.format(card_type)).click()

            with step(f'Заполнить поле "Cardholder name" значением: {cardholder_name}'):
                cardholder_name_field = self.find_element(*Locators.CARDHOLDER_NAME)
                self.send_keys(field=cardholder_name_field, value=cardholder_name)

            with step(f'Заполнить поле "Card number" значением: {card_number}'):
                card_number_field = self.find_element(*Locators.CARD_NUMBER)
                self.send_keys(field=card_number_field, value=card_number)

            with step(f'Выбрать месяц окончания действия карты: {card_expiration_month}'):
                self.find_element(*Locators.EXPIRATION_MONTH_LIST).click()

                strategy, locator = Locators.EXPIRATION_MONTH_LIST_OPTION_BY_NAME
                self.find_element(strategy, locator.format(card_expiration_month)).click()

            with step(f'Выбрать год окончания действия карты: {card_expiration_year}'):
                self.find_element(*Locators.EXPIRATION_YEAR_LIST).click()

                strategy, locator = Locators.EXPIRATION_YEAR_LIST_OPTION_BY_NAME
                self.find_element(strategy, locator.format(card_expiration_year)).click()

            with step(f'Заполнить поле "Card code" значением: {card_code}'):
                card_code_field = self.find_element(*Locators.CARD_CODE)
                self.send_keys(field=card_code_field, value=card_code)

        elif payment_method == 'Purchase Order':
            if is_random:
                purchase_order_number = randrange(1, 999999)

            with step(f'Заполнить поле "PO Number" значением: {purchase_order_number}'):
                purchase_order_number_field = self.find_element(*Locators.PURCHASE_ORDER_NUMBER)
                self.send_keys(field=purchase_order_number_field, value=purchase_order_number)

        with step('Кликнуть по кнопке "Continue"'):
            self.find_element_clickable(*Locators.PAYMENT_INFO_CONTINUE_BUTTON).click()

    @step('Подтвердить заказ')
    def confirm_order(self) -> None:
        """
        Подтвердить заказ.
        """

        self.find_element_clickable(*Locators.CONFIRM_ORDER_BUTTON).click()
