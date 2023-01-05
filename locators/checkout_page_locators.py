from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    """
    Локаторы для страницы создания заказа.
    """

    BILLING_COUNTRY_LIST = (By.ID, 'BillingNewAddress_CountryId')
    BILLING_COUNTRY_LIST_OPTION_BY_NAME = (
        By.XPATH,
        ".//select[@id='BillingNewAddress_CountryId']//option[text()='{0}']",
    )
    BILLING_STATE_LIST = (By.ID, 'BillingNewAddress_StateProvinceId')
    BILLING_STATE_LIST_OPTION_BY_NAME = (
        By.XPATH,
        ".//select[@id='BillingNewAddress_StateProvinceId']//option[text()='{0}']",
    )
    BILLING_CITY = (By.ID, 'BillingNewAddress_City')
    BILLING_ADDRESS = (By.ID, 'BillingNewAddress_Address1')
    BILLING_ZIP_CODE = (By.ID, 'BillingNewAddress_ZipPostalCode')
    BILLING_PHONE = (By.ID, 'BillingNewAddress_PhoneNumber')
    BILLING_CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "div[id='billing-buttons-container'] input.new-address-next-step-button",
    )
    STEP_SHIPPING = (By.ID, 'checkout-step-shipping')
    PICK_UP_IN_STORE_CHECKBOX = (By.ID, 'PickUpInStore')
    SHIPPING_ADDRESS_LIST = (By.ID, 'shipping-address-select')
    SHIPPING_ADDRESS_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='shipping-address-select']//option[text()='{0}']")
    SHIPPING_COUNTRY_LIST = (By.ID, 'ShippingNewAddress_CountryId')
    SHIPPING_COUNTRY_LIST_OPTION_BY_NAME = (
        By.XPATH,
        ".//select[@id='ShippingNewAddress_CountryId']//option[text()='{0}']",
    )
    SHIPPING_STATE_LIST = (By.ID, 'ShippingNewAddress_StateProvinceId')
    SHIPPING_STATE_LIST_OPTION_BY_NAME = (
        By.XPATH,
        ".//select[@id='ShippingNewAddress_StateProvinceId']//option[text()='{0}']",
    )
    SHIPPING_CITY = (By.ID, 'ShippingNewAddress_City')
    SHIPPING_ADDRESS = (By.ID, 'ShippingNewAddress_Address1')
    SHIPPING_ZIP_CODE = (By.ID, 'ShippingNewAddress_ZipPostalCode')
    SHIPPING_PHONE = (By.ID, 'ShippingNewAddress_PhoneNumber')
    SHIPPING_CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "div[id='shipping-buttons-container'] input.new-address-next-step-button",
    )
    STEP_SHIPPING_METHOD = (By.ID, 'checkout-step-shipping-method')
    SHIPPING_METHOD_RADIO_BUTTON_BY_NAME = (
        By.XPATH,
        ".//div[@id='checkout-step-shipping-method']//label[contains(text(), '{0}')]",
    )
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.shipping-method-next-step-button')
    PAYMENT_METHOD_RADIO_BUTTON_BY_NAME = (
        By.XPATH,
        ".//div[@id='checkout-payment-method-load']//label[contains(text(), '{0}')]",
    )
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.payment-method-next-step-button')
    CARD_TYPE_LIST = (By.ID, 'CreditCardType')
    CARD_TYPE_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='CreditCardType']//option[text()='{0}']")
    CARDHOLDER_NAME = (By.ID, 'CardholderName')
    CARD_NUMBER = (By.ID, 'CardNumber')
    EXPIRATION_MONTH_LIST = (By.ID, 'ExpireMonth')
    EXPIRATION_MONTH_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='ExpireMonth']//option[text()='{0}']")
    EXPIRATION_YEAR_LIST = (By.ID, 'ExpireYear')
    EXPIRATION_YEAR_LIST_OPTION_BY_NAME = (By.XPATH, ".//select[@id='ExpireYear']//option[text()='{0}']")
    CARD_CODE = (By.ID, 'CardCode')
    PURCHASE_ORDER_NUMBER = (By.ID, 'PurchaseOrderNumber')
    PAYMENT_INFO_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.payment-info-next-step-button')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, 'input.confirm-order-next-step-button')
