from allure import step

from locators import CheckoutCompletedPageLocators as Locators

from .base_page import BasePage


class CheckoutCompletedPage(BasePage):
    """
    Методы для работы со страницей завершения оформления заказа.
    """

    def __init__(self, driver):
        super().__init__(driver)

    path = 'checkout/completed/'

    @step('Проверить, что открыта страница завершения оформления заказа')
    def should_be_open_checkout_completed_page(self) -> None:
        """
        Проверка открытия страницы завершения оформления заказа.
        """

        self.should_be_open_page_by_path(path=self.path)

    @step('Проверить наличие сообщения об успешно созданном заказе')
    def can_see_message_about_successfully_creating_order(self) -> None:
        """
        Проверка наличия сообщения об успешно созданном заказе.
        """

        with step('Проверить, что сообщение появилось'):
            assert self.is_element_present(*Locators.MESSAGE_ABOUT_SUCCESSFULLY_CREATING_ORDER), \
                'На странице нет сообщения об успешном создании заказа'

        with step('Проверить текст сообщения'):
            expected_message_text = 'Your order has been successfully processed!'
            actual_message_text = self.find_element(*Locators.MESSAGE_ABOUT_SUCCESSFULLY_CREATING_ORDER).text
            assert actual_message_text.strip() == expected_message_text, \
                f'Текущий текст сообщения: {actual_message_text} не соответствует ожидаемому: {expected_message_text}'
