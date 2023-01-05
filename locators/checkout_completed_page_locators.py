from selenium.webdriver.common.by import By


class CheckoutCompletedPageLocators:
    """
    Локаторы для страницы завершения оформления заказа.
    """

    MESSAGE_ABOUT_SUCCESSFULLY_CREATING_ORDER = (By.CSS_SELECTOR, 'div.order-completed div.title')
