import pytest
from selene import browser
import os


WORK_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(WORK_DIR, 'resources')

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1200
    browser.config.window_width = 1200
    yield
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['ru_RU']
