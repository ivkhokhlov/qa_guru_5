import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['ru_RU']
