from selene import browser, by, be, have, command


class GitHubPage:

    def __init__(self):
        self.button_search = browser.element('.search-input')
        self.search = browser.element('#query-builder-test')
        self.actions = browser.element('#actions-tab')
        self.navigation = browser.element('.Button-content')

    def open(self):
        browser.open('https://github.com')
        return self

    def open_search(self):
        self.button_search.click()

    def fill_search(self, value: str):
        self.search.type(value).press_enter()

    @staticmethod
    def link_open(value: str):
        browser.element(by.link_text(value)).click()

    @staticmethod
    def search_text_click(value: str):
        browser.element(by.text(value)).click()

    @staticmethod
    def click_element(element):
        element.click()

    def open_actions(self):
        self.actions.click()

    @staticmethod
    def should_visible_text(value: str):
        browser.element(by.partial_text(value)).should(be.visible)
