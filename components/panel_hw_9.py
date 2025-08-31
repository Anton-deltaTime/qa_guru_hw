from selene import browser, have, command

from pages.page_hw_9 import StudentRegistrationPage, ProfilePage


class LeftPanel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def __open(self, parent, item):
        self.container.all('div.header-text').element_by(have.text(parent)).perform(command.js.scroll_into_view)
        self.container.all('div.header-text').element_by(have.text(parent)).element('..').element('..').click()
        self.container.all('span.text').element_by(have.text(item)).element('..').click()

    def open_profile_form(self):
        self.__open('Elements', 'Text Box')
        return ProfilePage()

    def open_student_registration_form(self):
        self.__open('Forms', 'Practice Form')
        return StudentRegistrationPage()
