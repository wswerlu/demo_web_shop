from locators import CheckoutAsGuestPageLocators as Locators
from utils.steps import step

from .base_page import BasePage


class CheckoutAsGuestPage(BasePage):
    """
    Методы для работы со страницей авторизации при создании заказа.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'login/checkoutasguest?returnUrl=%2Fcart'

    @step('Проверить, что открыта страница авторизации при создании заказа')
    def should_be_open_checkout_as_guest_page(self) -> None:
        """
        Проверка открытия страницы авторизации при создании заказа.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Кликнуть по кнопке "Checkout as Guest"')
    def click_on_checkout_as_guest_button(self) -> None:
        """
        Клик по кнопке "Checkout as Guest".
        """

        self.find_element_clickable(*Locators.CHECKOUT_AS_GUEST_BUTTON).click()
