import os
import random

from selene import browser, be, have


def test_fill_form(setup):
    print('')
    browser.open('https://demoqa.com/automation-practice-form')
    # Заполнение текстовых полей
    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')
    browser.element('#userEmail').type('new_email@example.ru')
    browser.element('#userNumber').type('8900123456')
    browser.element('#currentAddress').type('Некоторый тестовый домашний адрес')

    # Рандомный выбор пола
    gender = random.choice(browser.element('#genterWrapper').all('.custom-control.custom-radio.custom-control-inline'))
    c_gender = gender().text  # Гендер для проверки
    gender.click()

    # Проверка отображения календаря при нажатии на поле с датой
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker').should(be.visible)

    # Рандомный выбор года из выпадающего списка
    select_year = browser.element('select.react-datepicker__year-select')
    select_year.click()
    year = random.choice(select_year.all('option'))
    c_year = year().text  # Выбранный год
    year.click()
    select_year.click()  # Скрываем список

    # Рандомный выбор месяца из выпадающего списка
    select_month = browser.element('select.react-datepicker__month-select')
    select_month.click()
    month = random.choice(select_month.all('option'))
    c_month = month().text   # Выбранный месяц
    month.click()
    select_month.click()  # Скрываем список

    # Рандомный выбор дня на календаре
    weeks = browser.element('.react-datepicker__month')
    week = random.choice(weeks.all('.react-datepicker__week')[:-1])
    day = random.choice(week.all(f'[aria-label*={c_month}]'))
    c_day = day().text  # Выбранный день
    day.click()
    choice_date = f'{c_day} {c_month},{c_year}'  # Дата для проверки

    # Заполняем поле Subjects значением Computer Science
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # Рандомный выбор дня на хобби
    hobbies = random.choice(browser.element('#hobbiesWrapper').all('.custom-control.custom-checkbox.custom-control-inline'))
    c_hobbies = hobbies().text
    hobbies.click()

    # Заполняем поле State and City значениями Haryana и Panipat
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()

    # Загрузка файла
    path_file = os.path.abspath(os.path.join(os.getcwd(), 'any_files/file_hw_5.txt'))
    browser.element('#uploadPicture').send_keys(path_file)
    file_name = os.path.split(path_file)[-1]

    # Отправка формы
    browser.element('#submit').click()

    # Проверка полученной формы
    modal_show = browser.element('.fade.modal.show')
    modal_show.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    modal_show.element('tbody').all('td').even.should(have.exact_texts(
        'FirstName LastName',
        'new_email@example.ru',
        c_gender,
        '8900123456',
        choice_date,
        'Computer Science',
        c_hobbies,
        file_name,
        'Некоторый тестовый домашний адрес',
        'Haryana Panipat'
    ))
