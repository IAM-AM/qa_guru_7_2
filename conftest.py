import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="session")
def opening_browser():
    driver = webdriver.Chrome()
    driver.get('https://google.com')


@pytest.fixture()
def set_browser_windows_size():
    browser.driver.set_window_size(2560, 1440)

    print("Gets test user before test running")

    yield

    print("Removing test user")
