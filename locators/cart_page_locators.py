from selenium.webdriver.common.by import By


class CartPageLocators:
    """
    Локаторы для страницы корзины.
    """

    PRODUCTS = (By.CSS_SELECTOR, 'tr.cart-item-row')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'a.product-name')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.product-unit-price')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'input.qty-input')
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, 'span.product-subtotal')
