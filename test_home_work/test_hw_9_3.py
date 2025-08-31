from applications.application_hw_9 import app
from models.model_hw_9 import petr


def test_fill_registration_form(setup):
    print('')
    app.open()

    registration_page = app.left_panel.open_student_registration_form()
    file_path = 'any_files/file_hw_5.txt'
    registration_page.register(petr, file_path)
    registration_page.should_have_registered(petr, 'file_hw_5.txt')

    profile_page = app.left_panel.open_profile_form()
    profile_page.register(petr)
    profile_page.should_have_registered(petr)
