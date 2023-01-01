def presence_element_in_element_located(element, strategy, locator):
    """
    Ожидание проверки нахождения элемента внутри переданного элемента.

    :param element: веб-элемент в котором необходимо производить поиск.
    :param strategy: стратегия поиска элемента.
    :param locator: локатор элемента.
    :return: элемент или False.
    """

    def _predicate(driver):
        elements = element.find_elements(strategy, locator)
        if elements:
            return elements[0]
        return False

    return _predicate


def presence_elements_in_element_located(element, strategy, locator):
    """
    Ожидание проверки нахождения элементов внутри переданного элемента.

    :param element: веб-элемент в котором необходимо производить поиск.
    :param strategy: стратегия поиска элементов.
    :param locator: локатор элементов.
    :return: список элементов или False.
    """

    def _predicate(driver):
        elements = element.find_elements(strategy, locator)
        if elements:
            return elements
        return False

    return _predicate
