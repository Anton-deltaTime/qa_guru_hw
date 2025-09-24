import allure
from allure_commons.types import Severity
from pages.page_hw_10 import GitHubPage


@allure.tag("web", "smoke")
@allure.severity(Severity.CRITICAL)
@allure.epic("Репозиторий GitHub")
@allure.feature("Просмотр страницы Actions")
@allure.story("Поиск элемента среди активных процессов")
@allure.link("https://github.com", name="test_github")
def test_github_decorator(setup):
    print('')
    github_page = open_main_page()
    open_search(github_page)
    fill_search(github_page, 'eroshenkoam/allure-example')
    link_open(github_page, 'eroshenkoam/allure-example')
    open_actions(github_page)
    should_visible_text(github_page, '10798')


@allure.step("Открытие основной страницы github.com")
def open_main_page():
    github_page = GitHubPage().open()
    return github_page


@allure.step("Активировать поле поиска")
def open_search(github_page):
    github_page.open_search()


@allure.step("Поиск {value}")
def fill_search(github_page, value):
    github_page.fill_search(value)


@allure.step("Открыть страницу {value}")
def link_open(github_page, value):
    github_page.link_open(value)


@allure.step("Открыть страницу Actions")
def open_actions(github_page):
    github_page.open_actions()


@allure.step("Поиск текста {value} на странице")
def should_visible_text(github_page, value):
    github_page.should_visible_text(value)
