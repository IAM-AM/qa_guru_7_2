from conftest import *


def test_find_text_positive_test(opening_browser, set_browser_windows_size):
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_find_text_negative(opening_browser, set_browser_windows_size):
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('wqfsdfsfwe').press_enter()
    browser.element('[id="topstuff"]').should(have.text('Your search - wqfsdfsfwe - did not match any documents.'))









