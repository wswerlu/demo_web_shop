from random import choice

from allure import step

from locators import HeaderLocators as Locators

from .base_page import BasePage


class Header(BasePage):
    """
    Методы для работы с хедером.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Перейти на страницу регистрации')
    def go_to_register_page(self) -> None:
        """
        Переход на страницу регистрации.
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

    @step('Кликнуть по произвольной категории')
    def click_on_random_category_and_get_its_name(self) -> str:
        """
        Клик по произвольной категории с получением имени категории, по которой был произведен клик.

        :return: название категории, по которой был произведен клик.
        """

        category = choice(self.find_elements(*Locators.CATEGORIES))

        if self.is_element_present_in_element(category, *Locators.SUBLIST_FIRST_LEVEL, timeout=2):
            self.hover(category)

            sublist_categories = self.find_elements_in_element(category, *Locators.SUBLIST_CATEGORIES)
            sublist_category = choice([x for x in sublist_categories if x.text != 'Camera, photo'])
            sublist_category_name = sublist_category.text
            sublist_category.click()

            return sublist_category_name

        category_name = category.text
        category.click()

        return category_name
