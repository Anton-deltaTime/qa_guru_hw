import pytest
from selene import browser

from pages.page_hw_10 import GitHubPage


@pytest.fixture()
def screen_size(request, setup):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.sign_up_indirect
class TestGitHub:
    size_desktop = (1600, 1000)
    size_mobile = (412, 915)

    @pytest.mark.parametrize('screen_size', [size_desktop], indirect=True, ids=["desktop"])
    def test_github_sign_up_desktop(self, screen_size):
        print('')
        github_page = GitHubPage().open()

        github_page.search_text_click('Sign up')

    @pytest.mark.parametrize('screen_size', [size_mobile], indirect=True, ids=["mobile"])
    def test_github_sign_up_mobile(self, screen_size):
        print('')
        github_page = GitHubPage().open()

        github_page.click_element(github_page.navigation)
        github_page.search_text_click('Sign up')
