from selene import browser

from components.panel_hw_9 import LeftPanel
from pages.page_hw_9 import StudentRegistrationPage, ProfilePage


class ApplicationManager:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.simple_registration = StudentRegistrationPage()
        self.profile = ProfilePage()

    def open(self):
        browser.open('https://demoqa.com/elements')
        return self


app = ApplicationManager()
