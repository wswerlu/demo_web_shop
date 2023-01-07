from selenium.webdriver.common.by import By


class HeaderLocators:
    """
    Локаторы для хедера.
    """

    REGISTER_LINK = (By.CSS_SELECTOR, 'a.ico-register')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a.ico-logout')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a.ico-login')
    ACCOUNT_LINK = (By.XPATH, ".//a[@class='account' and text()='{0}']")
    CATEGORIES = (By.CSS_SELECTOR, 'ul.top-menu > li')
    SUBLIST_FIRST_LEVEL = (By.CSS_SELECTOR, 'ul.sublist.firstLevel')
    SUBLIST_CATEGORIES = (By.CSS_SELECTOR, 'ul.sublist.firstLevel a')
    PRODUCT_QUANTITY_IN_CART = (By.CSS_SELECTOR, 'a.ico-cart span.cart-qty')
    CART_LINK = (By.CSS_SELECTOR, 'a.ico-cart')
    PRODUCTS_IN_FLYOUT_CART = (By.CSS_SELECTOR, 'div.mini-shopping-cart div.item')
    PRODUCT_NAME_IN_FLYOUT_CART = (By.CSS_SELECTOR, 'div.name')
    PRODUCT_PRICE_IN_FLYOUT_CART = (By.CSS_SELECTOR, 'div.price span')
    PRODUCT_QUANTITY_IN_FLYOUT_CART = (By.CSS_SELECTOR, 'div.quantity span')
    PRODUCT_QUANTITY_IN_WISHLIST = (By.CSS_SELECTOR, 'a.ico-wishlist span.wishlist-qty')
    WISHLIST_LINK = (By.CSS_SELECTOR, 'a.ico-wishlist')
