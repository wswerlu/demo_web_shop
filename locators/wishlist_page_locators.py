from selenium.webdriver.common.by import By


class WishlistPageLocators:
    """
    Локаторы для страницы корзины.
    """

    PRODUCTS = (By.CSS_SELECTOR, 'tr.cart-item-row')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'td.product a')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.product-unit-price')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'input.qty-input')
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, 'span.product-subtotal')
    REMOVE_PRODUCT_BY_NAME = (By.XPATH, './/a[text()="{0}"]/../..//input[@name="removefromcart"]')
    UPDATE_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input.update-wishlist-button')
    EMPTY_WISHLIST_MESSAGE = (By.CSS_SELECTOR, 'div.wishlist-content')
    ADD_TO_CART_PRODUCT_BY_NAME = (By.XPATH, ".//a[text()='{0}']/../..//input[@name='addtocart']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'input.wishlist-add-to-cart-button')
