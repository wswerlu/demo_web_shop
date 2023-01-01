from allure import step

from locators import RegistrationPageLocators as Locators
from utils.generated_test_data import UserData

from .base_page import BasePage


class RegistrationPage(BasePage):
    """
    Методы для работы с хедером.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'register'

    @step('Проверить, что открыта страница регистрации')
    def should_be_open_registration_page(self) -> None:
        """
        Проверка открытия страницы регистрации.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Заполнить форму регистрации')
    def fill_registration_form(self, gender: str | None = None, firstname: str | None = None,
                               lastname: str | None = None, email: str | None = None, password: str | None = None,
                               confirm_password: str | None = None, is_random: bool = True) -> None:
        """
        Заполнение формы регистрации указанными данными.

        :param gender: пол ()
        :param firstname: имя.
        :param lastname: фамилия.
        :param email: email.
        :param password: пароль.
        :param confirm_password: данные для поля подтверждения пароля.
         Указывать в случае, если для теста значение этого поля должно отличаться от поля с паролем.
        :param is_random: True — нужен произвольный пользователь (остальные параметры указывать не надо),
         False — нужен пользователь с конкретными данными.
        """

        if is_random:
            user = UserData()
            gender = user.gender()
            firstname = user.firstname()
            lastname = user.lastname()
            email = user.email()
            password = user.password()

        if gender:
            with step(f'Выбрать пол: {gender}'):
                strategy, locator = Locators.GENDER_RADIO_BUTTON
                self.find_element(strategy, locator.format(gender)).click()

        with step(f'Заполнить поле "First name" значением: {firstname}'):
            firstname_field = self.find_element(*Locators.FIRSTNAME_FIELD)
            self.send_keys(field=firstname_field, value=firstname)

        with step(f'Заполнить поле "Last name" значением: {lastname}'):
            lastname_field = self.find_element(*Locators.LASTNAME_FIELD)
            self.send_keys(field=lastname_field, value=lastname)

        with step(f'Заполнить поле "Email" значением: {email}'):
            email_field = self.find_element(*Locators.EMAIL_FIELD)
            self.send_keys(field=email_field, value=email)

        with step(f'Заполнить поле "Password" значением: {password}'):
            password_field = self.find_element(*Locators.PASSWORD_FIELD)
            self.send_keys(field=password_field, value=password)

        with step(f'Заполнить поле "Confirm password" значением: {password}'):
            confirm_password_field = self.find_element(*Locators.CONFIRM_PASSWORD_FIELD)
            self.send_keys(
                field=confirm_password_field,
                value=password if confirm_password is None else confirm_password,
            )

    @step('Кликнуть по кнопке "Register"')
    def click_on_register_button(self) -> None:
        """
        Клик по кнопке "Register".
        """

        self.find_element_clickable(*Locators.REGISTER_BUTTON).click()
