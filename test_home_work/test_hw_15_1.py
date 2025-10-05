import pytest
from selene import browser

from pages.page_hw_10 import GitHubPage


@pytest.fixture(params=[(1600, 1000), (412, 915)], ids=['desktop', 'mobile'])
def screen_size(request, setup):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height
    return width, height


@pytest.mark.sign_up_if
class TestGitHub:

    def test_github_sign_up_desktop(self, screen_size):
        print('')
        width, height = screen_size
        if (width, height) < (1200, 900):
            pytest.skip(reason='Размеры экрана не десктопные')
        github_page = GitHubPage().open()

        github_page.search_text_click('Sign up')

    def test_github_sign_up_mobile(self, screen_size):
        print('')
        width, height = screen_size
        if (width, height) >= (1200, 900):
            pytest.skip(reason='Размеры экрана не десктопные')
        github_page = GitHubPage().open()

        github_page.click_element(github_page.navigation)
        github_page.search_text_click('Sign up')
