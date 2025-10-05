import pytest
from selene import browser

from pages.page_hw_10 import GitHubPage


@pytest.fixture()
def screen_size_desktop(setup):
    width, height = (1600, 1000)
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture()
def screen_size_mobile(setup):
    width, height = (412, 915)
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.sign_up_fixture
class TestGitHub:

    def test_github_sign_up_desktop(self, screen_size_desktop):
        print('')
        github_page = GitHubPage().open()

        github_page.search_text_click('Sign up')

    def test_github_sign_up_mobile(self, screen_size_mobile):
        print('')
        github_page = GitHubPage().open()

        github_page.click_element(github_page.navigation)
        github_page.search_text_click('Sign up')
