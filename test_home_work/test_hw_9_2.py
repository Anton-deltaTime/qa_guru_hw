from pages.page_hw_9 import StudentRegistrationPage
from models.model_hw_9 import petr


def test_fill_registration_form(setup):
    print('')
    registration_page = StudentRegistrationPage().open()

    file_path = 'any_files/file_hw_5.txt'
    registration_page.register(petr, file_path)

    registration_page.should_have_registered(petr, 'file_hw_5.txt')
