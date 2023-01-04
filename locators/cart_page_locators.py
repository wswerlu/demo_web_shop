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
    REMOVE_PRODUCT_BY_NAME = (By.XPATH, ".//a[text()='{0}']/../..//input[@name='removefromcart']")
    UPDATE_SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, 'input.update-cart-button')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div.order-summary-content')
