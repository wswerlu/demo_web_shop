from random import choice

from mimesis import Person


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
