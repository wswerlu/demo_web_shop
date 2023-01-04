from selenium.webdriver.common.by import By


class ProductCardPageLocators:
    """
    Локаторы для страницы карточки продукта.
    """

    ATTRIBUTES_BLOCK = (By.CSS_SELECTOR, 'div.product-essential div.attributes')
    ATTRIBUTES = (By.CSS_SELECTOR, 'div.product-essential div.attributes dd')
    RADIO_BUTTON = (By.CSS_SELECTOR, "input[type='radio']")
    SELECT_ELEMENT = (By.CSS_SELECTOR, 'select')
    SELECT_OPTION = (By.CSS_SELECTOR, 'option')
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    GIFTCARD_ATTRIBUTES_BLOCK = (By.CSS_SELECTOR, 'div.product-essential div.giftcard')
    RECIPIENT_NAME = (By.CSS_SELECTOR, 'input.recipient-name')
    RECIPIENT_EMAIL = (By.CSS_SELECTOR, 'input.recipient-email')
    SENDER_NAME = (By.CSS_SELECTOR, 'input.sender-name')
    SENDER_EMAIL = (By.CSS_SELECTOR, 'input.sender-email')
    GIFTCARD_MESSAGE = (By.CSS_SELECTOR, 'textarea.message')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'input.qty-input')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'input.add-to-cart-button')
    MESSAGE_ABOUT_ADDING_PRODUCT_TO_CART = (By.ID, 'bar-notification')
    PRODUCT_ID = (By.CSS_SELECTOR, 'div[data-productid]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product-name')
    PRODUCT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, 'div.short-description')
    PRODUCT_FULL_DESCRIPTION = (By.CSS_SELECTOR, 'div.full-description')
    PRODUCT_OLD_PRICE = (By.CSS_SELECTOR, 'div.old-product-price span')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product-price span')
