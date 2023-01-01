from importlib import import_module

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.helpers import get_fixtures

pytest_plugins = get_fixtures()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'],
                     help='Set browser to launch')
    parser.addoption('--maximized', action='store_true', default=True, help='Maximize browser window')


@fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser')
    maximized = request.config.getoption('maximized')

    driver = None

    if browser_name == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    if maximized:
        driver.maximize_window()

    yield driver

    driver.quit()


def pytest_generate_tests(metafunc):
    for fixture_name in metafunc.fixturenames:
        if fixture_name.startswith('data_'):
            module, data = fixture_name[5:].split('_')
            testdata = load_from_module(module, data)
            metafunc.parametrize(fixture_name, testdata, ids=[str(x[-1]) for x in testdata])


def load_from_module(module, data):
    return getattr(import_module(f'data.parametrization.{module}'), data)
