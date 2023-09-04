from selene.support.shared import browser
from selene import be, have

def test_google_should_finde_text(set_browser_size, clear_field):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_google_should_find_text(set_browser_size, clear_field):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ghosafnLNSFENFOINCNKSADSLknkn').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))