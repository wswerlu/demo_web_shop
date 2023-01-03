from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Локаторы для страницы авторизации.
    """

    REGISTER_LINK = (By.CSS_SELECTOR, 'a.ico-register')
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    REMEMBER_ME = (By.ID, 'RememberMe')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.validation-summary-errors')
