from pages.page_hw_9 import StudentRegistrationPage


def test_fill_registration_form(setup):
    print('')
    registration_page = StudentRegistrationPage().open()

    registration_page.fill_first_name('FirstName')
    registration_page.fill_last_name('LastName')
    registration_page.fill_user_email('new_email@example.ru')
    registration_page.choose_gender('Male')
    registration_page.fill_mobile_number('8900123456')
    registration_page.choose_date_of_birth('30', 'April', '1995')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Reading')
    file_path = 'any_files/file_hw_5.txt'
    registration_page.fill_picture(file_path)
    registration_page.fill_current_address('Некоторый тестовый домашний адрес')
    registration_page.fill_state_and_city('Haryana', 'Panipat')

    registration_page.submit_form()

    registration_page.check_registration_form(
        'FirstName LastName',
        'new_email@example.ru',
        'Male',
        '8900123456',
        '30 April,1995',
        'Computer Science',
        'Reading',
        'file_hw_5.txt',
        'Некоторый тестовый домашний адрес',
        'Haryana Panipat'
    )
