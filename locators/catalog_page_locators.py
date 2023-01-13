from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """
    Локаторы для хедера.
    """

    TITLE = (By.CSS_SELECTOR, 'div.page-title')
    PRODUCTS = (By.CSS_SELECTOR, 'div.item-box')
    PRODUCT_ID = (By.CSS_SELECTOR, 'div.product-item')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h2.product-title a')
    PRODUCT_ACTUAL_PRICE = (By.CSS_SELECTOR, 'div.prices span.actual-price')
    PRODUCT_OLD_PRICE = (By.CSS_SELECTOR, 'div.prices span.old-price')
    GO_TO_PRODUCT_CARD_BY_ID = (By.CSS_SELECTOR, "div[data-productid='{0}'] a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'input.product-box-add-to-cart-button')
    SORT_METHOD_LIST = (By.ID, 'products-orderby')
    SORT_METHOD_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='products-orderby']//option[text()='{0}']")
    PAGE_SIZE_LIST = (By.ID, 'products-pagesize')
    PAGE_SIZE_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='products-pagesize']//option[text()='{0}']")
    BUTTONS_BLOCK_BY_PRODUCT_NAME = (By.XPATH, './/a[text()="{0}"]/../..//div[@class="buttons"]')
    BODY = (By.CSS_SELECTOR, 'body')
