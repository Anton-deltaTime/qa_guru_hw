from functools import partial
import os
import pytest
import subprocess

import allure
from dotenv import load_dotenv
import requests
from selene import browser
from selenium import webdriver

from utils import attach

DEFAULT_BROWSER_VERSION = "127.0"


def pytest_addoption(parser):
    parser.addoption("--loc", action="store", default="local", help="'local' or 'jenkins', test launch location")
    parser.addoption("--browser_version", action="store", default="127.0")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='module')
def setup(request):
    get_location = request.config.getoption("--loc")

    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    options.add_argument('Content-Type=text/plain;charset=UTF-8')
    options.add_argument('Connection=keep-alive')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')

    if get_location == 'jenkins':
        browser_version = request.config.getoption("--browser_version")
        browser_version = browser_version if browser_version else DEFAULT_BROWSER_VERSION

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_password = os.getenv("SELENOID_PASSWORD")
        selenoid_url = os.getenv("SELENOID_URL")
        with allure.step('Настройка selenoid для options'):
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True,
                    "enableLog": True
                }
            }
            options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}",
            options=options)
        browser.config.driver = driver

    browser.config.driver_options = options
    browser.config.window_width = 1600
    browser.config.window_height = 1000
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def send_request(request):
    with allure.step('Подготовка запроса в API reqres.in'):
        method = request.param[0]
        endpoint = request.param[1]

        headers = {"x-api-key": "reqres-free-v1"}
        url = f"https://reqres.in/{endpoint}"

        request = partial(getattr(requests, method), url=url, headers=headers)
    return request


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
