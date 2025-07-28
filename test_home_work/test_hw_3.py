import random
import string

from selene import browser, be, by, have


def test_search_true(setup):
    browser.open('https://ya.ru/')
    # Проблема showcaptcha решается переоткрыванием вкладки
    if browser.element('html').wait_until(have.text('Подтвердите, что запросы отправляли вы, а не робот')):
        browser.open('https://ya.ru/')
    browser.element(by.id('text')).should(be.blank)
    browser.element(by.id('text')).type('python selene').press_enter()
    browser.element(by.id('search-result')).should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_search_false(setup):
    browser.open('https://ya.ru/')
    # Проблема showcaptcha решается переоткрыванием вкладки
    if browser.element('html').wait_until(have.text('Подтвердите, что запросы отправляли вы, а не робот')):
        browser.open('https://ya.ru/')
    browser.element(by.id('text')).should(be.blank)
    # Генерация случайного набора символов ascii длинной 15
    random_text = ''.join(random.choices(string.ascii_letters, k=15))
    browser.element(by.id('text')).type(random_text).press_enter()
    browser.element('html').should(have.text('Ничего не нашли'))
