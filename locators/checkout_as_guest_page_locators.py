from selenium.webdriver.common.by import By


class CheckoutAsGuestPageLocators:
    """
    Локаторы для страницы авторизации при создании заказа.
    """

    CHECKOUT_AS_GUEST_BUTTON = (By.CSS_SELECTOR, 'input.checkout-as-guest-button')
