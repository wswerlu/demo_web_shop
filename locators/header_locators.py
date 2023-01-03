from selenium.webdriver.common.by import By


class HeaderLocators:
    """
    Локаторы для хедера.
    """

    REGISTER_LINK = (By.CSS_SELECTOR, 'a.ico-register')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a.ico-logout')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a.ico-login')
    ACCOUNT_LINK = (By.XPATH, ".//a[@class='account' and text()='{0}']")
