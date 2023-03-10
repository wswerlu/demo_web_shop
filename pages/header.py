from locators import HeaderLocators as Locators
from utils.steps import step

from .base_page import BasePage


class Header(BasePage):
    """
    Методы для работы с хедером.
    """

    def __init__(self, driver):
        super().__init__(driver)

    @step('Перейти на страницу регистрации')
    def go_to_register_page(self) -> None:
        """
        Переход на страницу регистрации.
        """

        self.find_element(*Locators.REGISTER_LINK).click()

    @step('Выйти из профиля пользователя')
    def logout_user(self) -> None:
        """
        Выход из профиля пользователя.
        """

        self.find_element(*Locators.LOGOUT_LINK).click()

    @step('Перейти на страницу авторизации')
    def go_to_login_page(self) -> None:
        """
        Переход на страницу авторизации.
        """

        self.find_element(*Locators.LOGIN_LINK).click()

    @step('Проверить, что в хедере отображается email: {email}')
    def can_see_user_email(self, email: str) -> None:
        """
        Проверка того, что в хедере отображается указанный email.
        """

        strategy, locator = Locators.ACCOUNT_LINK

        assert self.is_element_present(strategy, locator.format(email)), \
            f'В хедере не отображается email: {email}'

    @step('Кликнуть по категории: "{category_name}"')
    def click_on_category_with_name(self, category_name: str) -> None:
        """
        Клик по произвольной категории с получением имени категории, по которой был произведен клик.

        :param category_name: название категории.
        """

        strategy, locator = Locators.MAIN_CATEGORY_BY_SUBCATEGORY_NAME

        if self.is_element_present(strategy, locator.format(category_name), timeout=0):
            main_category = self.find_element(strategy, locator.format(category_name), timeout=0)
            self.hover(main_category)

        strategy, locator = Locators.CATEGORY_BY_NAME
        self.find_visible_element(strategy, locator.format(category_name), timeout=2).click()

    @step('Проверить, что в хедере отображается количество товара в корзине')
    def can_see_product_quantity_in_cart(self, expected_quantity: int = 1) -> None:
        """
        Проверка того, что в хедере отображается количество товара в корзине.

        :param expected_quantity: ожидаемое количество товара в корзине.
        """

        actual_quantity = self.find_element(*Locators.PRODUCT_QUANTITY_IN_CART).text[1:-1]

        assert int(actual_quantity) == expected_quantity, \
            f'Текущее значение количества товара в корзине: {actual_quantity} ' \
            f'не соответствует ожидаемому: {expected_quantity}'

    @step('Перейти на страницу корзины')
    def go_to_cart_page(self) -> None:
        """
        Переход на страницу корзины.
        """

        self.find_element(*Locators.CART_LINK).click()

    def get_products_in_flyout_cart(self) -> list:
        """
        Получение товаров во всплывающей корзине.
        """

        flyout_cart = self.find_element(*Locators.CART_LINK)
        self.hover(flyout_cart)

        products = self.find_visible_elements(*Locators.PRODUCTS_IN_FLYOUT_CART)

        products_list = []

        for product in products:

            name = self.find_element_in_element(product, *Locators.PRODUCT_NAME_IN_FLYOUT_CART).text
            price = self.find_element_in_element(product, *Locators.PRODUCT_PRICE_IN_FLYOUT_CART).text
            quantity = self.find_element_in_element(product, *Locators.PRODUCT_QUANTITY_IN_FLYOUT_CART).text

            products_list.append(
                {
                    'name': name,
                    'price': float(price),
                    'quantity': int(quantity),
                },
            )

        return products_list

    @step('Проверить, что товар отображается во всплывающей корзине')
    def can_see_product_in_flyout_cart(self, product_names: str | list) -> None:
        """
        Проверка того, что товар отображается во всплывающей корзине.

        :param product_names: наименования товаров, которые должны быть в корзине.
        """

        if not isinstance(product_names, list):
            product_names = [product_names]

        product_names_in_cart = [x['name'] for x in self.get_products_in_flyout_cart()]

        for product_name in product_names:
            assert product_name in product_names_in_cart, f'В корзине нет товара {product_name!r}'

    @step('Проверить, что в хедере отображается количество товара в вишлисте')
    def can_see_product_quantity_in_wishlist(self, expected_quantity: int = 1) -> None:
        """
        Проверка того, что в хедере отображается количество товара в корзине.

        :param expected_quantity: ожидаемое количество товара в вишлисте.
        """

        actual_quantity = self.find_element(*Locators.PRODUCT_QUANTITY_IN_WISHLIST).text[1:-1]

        assert int(actual_quantity) == expected_quantity, \
            f'Текущее значение количества товара в корзине: {actual_quantity} ' \
            f'не соответствует ожидаемому: {expected_quantity}'

    @step('Перейти на страницу вишлиста')
    def go_to_wishlist_page(self) -> None:
        """
        Переход на страницу корзины.
        """

        self.find_element(*Locators.WISHLIST_LINK).click()
