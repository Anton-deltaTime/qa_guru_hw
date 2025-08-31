import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='module')
def setup():
    # Добавление заголовков (иногда достаточный минимум для адекватной реакции браузера на тесты)
    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    options.add_argument('Content-Type=text/plain;charset=UTF-8')
    options.add_argument('Connection=keep-alive')
    browser.config.driver_options = options

    browser.config.window_width = 1600
    browser.config.window_height = 1000
    yield
    browser.quit()
