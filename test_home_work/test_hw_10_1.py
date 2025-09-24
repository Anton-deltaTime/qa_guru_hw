from pages.page_hw_10 import GitHubPage


def test_github(setup):
    print('')
    github_page = GitHubPage().open()

    github_page.open_search()
    github_page.fill_search('eroshenkoam/allure-example')
    github_page.link_open('eroshenkoam/allure-example')
    github_page.open_actions()
    github_page.should_visible_text('10798')
