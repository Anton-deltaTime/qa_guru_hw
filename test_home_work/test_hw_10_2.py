import allure
from allure_commons.types import Severity
from pages.page_hw_10 import GitHubPage


def test_github_steps(setup):
    print('')
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.epic('Репозиторий GitHub')
    allure.dynamic.feature("Просмотр страницы Actions")
    allure.dynamic.story("Поиск элемента среди активных процессов")
    allure.dynamic.link("https://github.com", name="test_github")
    with allure.step('Открытие основной страницы github.com'):
        github_page = GitHubPage().open()

    with allure.step('Активировать поле поиска'):
        github_page.open_search()

    with allure.step('Поиск eroshenkoam/allure-example'):
        github_page.fill_search('eroshenkoam/allure-example')

    with allure.step('Открыть страницу eroshenkoam/allure-example'):
        github_page.link_open('eroshenkoam/allure-example')

    with allure.step('Открыть страницу Actions'):
        github_page.open_actions()

    with allure.step('Поиск текста "10798" на странице'):
        github_page.should_visible_text('10798')
