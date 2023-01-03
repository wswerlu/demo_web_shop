from selenium.webdriver.common.by import By


class RegistrationSuccessPageLocators:
    """
    Локаторы для страницы подтверждения регистрации.
    """

    CONFIRM_MESSAGE = (By.CSS_SELECTOR, 'div.result')
