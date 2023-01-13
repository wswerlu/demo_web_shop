from selenium.webdriver.common.by import By


class NotificationBarLocators:
    """
    Локаторы для панели уведомлений.
    """

    NOTIFICATION_ABOUT_ADDING_PRODUCT = (By.ID, 'bar-notification')
    CLOSE_NOTIFICATION = (By.CSS_SELECTOR, "[id='bar-notification'] span.close")
