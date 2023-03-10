from typing import List

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils import own_expected_conditions as oec


class BasePage:
    def __init__(self, driver, base_url='https://demowebshop.tricentis.com/'):
        self.driver = driver
        self.base_url = base_url

    def open(self, path: str = '') -> None:
        """
        Открыть страницу.

        :param path: эндпоинт страницы, на которую нужно перейти.
        """
        self.driver.get(self.base_url + path)

    def refresh(self) -> None:
        """
        Обновить страницу.
        """
        self.driver.refresh()

    def switch_to_other_tab(self, tab_index=1) -> None:
        """
        Переключение на другую вкладку.

        :param tab_index: индекс вкладки, на которую нужно переключиться.
        """
        other_tab = self.driver.window_handles[tab_index]
        self.driver.switch_to.window(other_tab)

    def scroll_to_element(self, element) -> None:
        """
        Скролл страницы до указанного элемента, чтобы он был в области видимости.

        :param element: элемент, до которого нужно проскроллить страницу.
        """
        self.driver.execute_script('arguments[0].scrollIntoView(false);', element)

    def scroll_to_element_center(self, element) -> None:
        """
        Скролл страницы до центра указанного элемента.

        :param element: элемент, до центра которого нужно проскроллить страницу.
        """
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    def is_element_present(self, strategy, locator, timeout=5) -> bool:
        """
        Проверка существования элемента на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: True или False.
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, strategy, locator, timeout=5) -> bool:
        """
        Проверка отсутствия элемента на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: True или False.
        """
        try:
            WebDriverWait(self.driver, timeout).until_not(ec.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, strategy, locator, timeout=5) -> bool:
        """
        Проверка видимости элемента на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: True или False.
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_visible(self, strategy, locator, timeout=5) -> bool:
        """
        Проверка невидимости элемента на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: True или False.
        """
        try:
            WebDriverWait(self.driver, timeout).until_not(ec.visibility_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def is_element_present_in_element(self, element, strategy, locator, timeout=5) -> bool:
        """
        Проверка существования элемента внутри указанного элемента.

        :param element: элемент, внутри которого нужно проверить наличие элемента.
        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: элемент.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                oec.presence_element_in_element_located(element, strategy, locator),
            )
        except TimeoutException:
            return False
        return True

    def find_element(self, strategy, locator, timeout=5) -> WebElement:
        """
        Поиск элемента на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: элемент.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            raise AssertionError(f'В течение {timeout} секунд не был найден элемент с локатором: {(strategy, locator)}')

    def find_elements(self, strategy, locator, timeout=5) -> List[WebElement]:
        """
        Поиск элементов на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: список элементов.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located((strategy, locator)))
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не были найдены элементы с локатором: {(strategy, locator)}',
            )

    def find_visible_element(self, strategy, locator, timeout=5) -> WebElement:
        """
        Поиск видимого элементов на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: элемент.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((strategy, locator)))
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не отображался элемент с локатором: {(strategy, locator)}',
            )

    def find_visible_elements(self, strategy, locator, timeout=5) -> List[WebElement]:
        """
        Поиск видимых элементов на странице.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: список элементов.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located((strategy, locator)))
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не отображались элементы с локатором: {(strategy, locator)}',
            )

    def find_element_clickable(self, strategy, locator, timeout=5) -> WebElement:
        """
        Поиск элемента, по которому можно кликнуть.

        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: элемент.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((strategy, locator)))
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не был доступен для клика элемент с локатором: {(strategy, locator)}',
            )

    def find_element_in_element(self, element, strategy, locator, timeout=5) -> WebElement:
        """
        Поиск элемента внутри указанного элемента.

        :param element: элемент, внутри которого нужно найти элемент.
        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: элемент.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                oec.presence_element_in_element_located(element, strategy, locator),
            )
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не был найден элемент с локатором: {(strategy, locator)} '
                f'внутри элемента: {element}',
            )

    def find_elements_in_element(self, element, strategy, locator, timeout=5) -> List[WebElement]:
        """
        Поиск элементов внутри указанного элемента.

        :param element: элемент, внутри которого нужно найти элементы.
        :param strategy: способ поиска элемента.
        :param locator: локатор.
        :param timeout: время ожидания.
        :return: список элементов.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                oec.presence_elements_in_element_located(element, strategy, locator),
            )
        except TimeoutException:
            raise AssertionError(
                f'В течение {timeout} секунд не были найдены элементы с локатором: {(strategy, locator)} '
                f'внутри элемента: {element}',
            )

    def switch_to_alert(self, timeout=5) -> Alert:
        """
        Переключение на алерт.

        :param timeout: время ожидания.
        :return: алерт.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
        except TimeoutException:
            raise AssertionError(f'В течение {timeout} секунд не появился алерт')

    @staticmethod
    def send_keys(field, value) -> None:
        """
        Заполнение поля указанным значением.

        :param field: поле, которое необходимо заполнить.
        :param value: значение поля.
        """
        field.click()
        field.clear()
        field.send_keys(value)

    def is_change_url_to_path(self, path, timeout=5):
        """
        Проверка открытия страницы.

        :param path: эндпоинт страницы.
        :param timeout: время ожидания.
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.url_to_be(self.base_url + path))
        except TimeoutException:
            return False
        return True

    def should_be_open_page_by_path(self, path) -> None:
        """
        Проверка открытия страницы.

        :param path: эндпоинт страницы.
        """

        # получение текущего и ожидаемого url`ов страницы, для понятного отображения ошибки
        actual_current_url = self.driver.current_url
        expected_current_url = self.base_url + path

        assert self.is_change_url_to_path(path=path), \
            f'Текущий url: {actual_current_url} не совпадает с ожидаемым: {expected_current_url}'

    def hover(self, element) -> None:
        """
        Ховер на элемент.

        :param element: элемент, на который нужно навести курсор.
        """
        ActionChains(self.driver).move_to_element(element).perform()
