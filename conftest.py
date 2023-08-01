import pytest
from selene import browser, be, have
from selene.core import query


@pytest.fixture(scope="session")
def opening_browser():
    pass


@pytest.fixture()
def set_browser_windows_size():
    browser.driver.set_window_size(2560, 1440)

    yield

    browser.get(query.screenshot_saved(path="/Users/aliaksandr.manko/Desktop/test_screenshots"))
