from random import choice

from mimesis import Address, Payment, Person, Text

from data.data import CREDIT_CARD_TYPE


class UserData:

    def __init__(self):
        self.person = Person('ru')

    def firstname(self) -> str:
        """
        Генерация имени.
        """
        return self.person.name()

    def lastname(self) -> str:
        """
        Генерация фамилии.
        """
        return self.person.last_name()

    def email(self) -> str:
        """
        Генерация email'а.
        """
        return self.person.email()

    def password(self) -> str:
        """
        Генерация пароля.
        """
        return self.person.password()

    @staticmethod
    def gender() -> str | None:
        """
        Генерация пола.
        """
        return choice(['Male', 'Female', None])

    def phone(self):
        """
        Генерация номера телефона.
        """
        return self.person.telephone(mask='+7##########')


class TextData:

    def __init__(self):
        self.text = Text('ru')

    def sentence(self):
        """
        Генерация предложения.
        """
        return self.text.sentence()


class AddressData:

    def __init__(self):
        self.address = Address('ru')

    def city(self) -> str:
        """
        Генерация города.
        """
        return self.address.city()

    def full_address(self) -> str:
        """
        Генерация полного адреса.
        """
        return self.address.address()

    def postal_code(self) -> str:
        """
        Генерация почтового индекса.
        """
        return self.address.postal_code()


class PaymentData:

    def __init__(self):
        self.payment = Payment()
        self.person = Person('en')

    def cardholder_name(self) -> str:
        """
        Генерация имени держателя карты.
        """
        return self.person.full_name()

    def card_number(self, card_type: str) -> str:
        """
        Генерация номера карты.

        :param card_type: тип карты. Допустимые значения: Visa, Master сard, Amex, Discover.
        """
        return self.payment.credit_card_number(card_type=CREDIT_CARD_TYPE[card_type])

    def card_code(self) -> str:
        """
        Генерация CVV кода карты.
        """
        return self.payment.cvv()
