from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(scope = 'session')
def set_browser_size():
    browser.config.window_height = 1920
    browser.config.window_width = 1080

@pytest.fixture(scope= 'function')
def clear_field():
    yield
    browser.element('[name="q"]').clear()