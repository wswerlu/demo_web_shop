from allure import step

from locators import LoginPageLocators as Locators

from .base_page import BasePage


class LoginPage(BasePage):
    """
    Методы для работы с хедером.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'login'

    @step('Проверить, что открыта страница авторизации')
    def should_be_open_login_page(self) -> None:
        """
        Проверка открытия страницы авторизации.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Заполнить форму авторизации')
    def fill_login_form(self, email: str, password: str, is_need_remember: bool = True) -> None:
        """
        Заполнение формы авторизации указанными данными.

        :param email: email.
        :param password: пароль.
        :param is_need_remember: True — включить флаг "Remember me?", False — не включать флаг "Remember me?".
        """

        with step(f'Заполнить поле "Email" значением: {email}'):
            email_field = self.find_element(*Locators.EMAIL_FIELD)
            self.send_keys(field=email_field, value=email)

        with step(f'Заполнить поле "Password" значением: {password}'):
            password_field = self.find_element(*Locators.PASSWORD_FIELD)
            self.send_keys(field=password_field, value=password)

        if is_need_remember:
            with step('Включить флаг "Remember me?"'):
                self.find_element(*Locators.REMEMBER_ME).click()

    @step('Кликнуть по кнопке "Log in"')
    def click_on_login_button(self) -> None:
        """
        Клик по кнопке "Log in".
        """

        self.find_element_clickable(*Locators.LOGIN_BUTTON).click()
