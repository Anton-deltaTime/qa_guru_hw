import pytest
import subprocess

from selene import browser
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--loc", action="store", default="local", choices=['local', 'jenkins'], help="'local' or 'jenkins', test launch location")


@pytest.fixture(scope='module')
def setup():
    # Добавление заголовков (иногда достаточный минимум для адекватной реакции браузера на тесты)
    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    options.add_argument('Content-Type=text/plain;charset=UTF-8')
    options.add_argument('Connection=keep-alive')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    browser.config.driver_options = options

    browser.config.window_width = 1600
    browser.config.window_height = 1000
    yield
    browser.quit()


def pytest_sessionfinish(session, exitstatus):
    """Генерация отчета Allure после запуска тестов (для локального запуска)"""
    env = session.config.getoption('--loc', default='local')
    if env == 'local':
        print('Генерация Allure-отчета...')
        try:
            subprocess.run(
                [r".\allure\bin\allure", "generate", "allure-results/", "--clean", "--single-file"],
                check=True,
                shell=True
            )
            print('ALlure-отчет успешно сгенерирован')
        except subprocess.CalledProcessError as e:
            print(f"Ошибка генерации Allure-отчета: {e}")
