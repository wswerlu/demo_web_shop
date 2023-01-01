from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """
    Локаторы для хедера.
    """

    GENDER_RADIO_BUTTON = (By.XPATH, ".//div[@class='gender']//label[text()='{0}']")
    FIRSTNAME_FIELD = (By.ID, 'FirstName')
    LASTNAME_FIELD = (By.ID, 'LastName')
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
    REGISTER_BUTTON = (By.ID, 'register-button')
