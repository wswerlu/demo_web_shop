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

    @step('Выйти из профиля пользователя')
    def logout_user(self) -> None:
        """
        Выход из профиля пользователя.
        """

        self.find_element(*Locators.LOGOUT_LINK).click()

    @step('Перейти на страницу авторизации')
    def go_to_login_page(self) -> None:
        """
        Переход на страницу авторизации.
        """

        self.find_element(*Locators.LOGIN_LINK).click()

    @step('Проверить, что в хедере отображается email: {email}')
    def can_see_user_email(self, email: str) -> None:
        """
        Проверка того, что в хедере отображается указанный email.
        """

        strategy, locator = Locators.ACCOUNT_LINK

        assert self.is_element_present(strategy, locator.format(email)), \
            f'В хедере не отображается email: {email}'
