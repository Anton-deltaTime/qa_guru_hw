import os

from selene import browser, be, have, command

from models.model_hw_9 import User


class StudentRegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.mobile_number = browser.element('#userNumber')
        self.current_address = browser.element('#currentAddress')
        self.gender = browser.element('#genterWrapper')
        self.date_of_birth = browser.element('#dateOfBirth')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbiesWrapper')
        self.upload_picture = browser.element('#uploadPicture')
        self.state_and_city = browser.element('#stateCity-wrapper')
        self.submit = browser.element('#submit')
        self.modal_show = browser.element('.fade.modal.show')
        self.close = browser.element('#closeLargeModal')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def submit_form(self):
        self.submit.perform(command.js.scroll_into_view)
        self.submit.click()

    def close_form(self):
        self.close.click()

    def fill_first_name(self, value: str):
        self.first_name.type(value)

    def fill_last_name(self, value: str):
        self.last_name.type(value)

    def fill_user_email(self, value: str):
        self.user_email.type(value)

    def fill_mobile_number(self, value: str):
        self.mobile_number.type(value)

    def fill_current_address(self, value: str):
        self.current_address.type(value)

    def choose_gender(self, value: str):
        self.gender.all('[name="gender"]').element_by(have.value(value)).element('..').click()

    def choose_date_of_birth(self, day: str, month: str, year: str):
        self.date_of_birth.element('#dateOfBirthInput').click()
        self.date_of_birth.element('.react-datepicker').should(be.visible)
        self.date_of_birth.element('select.react-datepicker__year-select').type(year)
        self.date_of_birth.element('select.react-datepicker__month-select').type(month)
        self.date_of_birth.all('.react-datepicker__day:not(.react-datepicker__day--outside-month)').element_by(have.text(day)).click()

    def fill_subjects(self, value: str):
        self.subjects.type(value).press_enter()

    def fill_hobbies(self, value: str):
        self.hobbies.all('.custom-control-label').element_by(have.text(value)).element('..').click()

    def fill_picture(self, value: str):
        path_file = os.path.abspath(os.path.join(os.getcwd(), value))
        self.upload_picture.send_keys(path_file)

    def fill_state_and_city(self, state: str, city: str):
        self.state_and_city.perform(command.js.scroll_into_view)
        self.state_and_city.element('#react-select-3-input').type(state).press_enter()
        self.state_and_city.element('#react-select-4-input').type(city).press_enter()

    def check_registration_form(self, full_name, email, gender, mobile, birthday, subjects, hobbies, picture, address, state_and_city):
        self.modal_show.element('tbody').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile,
            birthday,
            subjects,
            hobbies,
            picture,
            address,
            state_and_city
        ))

    def register(self, user: User, file_path: str):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_user_email(user.email)
        self.choose_gender(user.gender.value)
        self.fill_mobile_number(user.mobile_number)
        day, month, year = user.birthday.strftime('%d'), user.birthday.strftime('%B'), user.birthday.strftime('%Y')
        self.choose_date_of_birth(day, month, year)
        self.fill_subjects(user.subjects)
        self.fill_hobbies(user.hobbies.value)
        self.fill_picture(file_path)
        self.fill_current_address(user.current_address)
        self.fill_state_and_city(user.state, user.city)
        self.submit_form()

    def should_have_registered(self, user: User, file_name: str):
        self.check_registration_form(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender.value,
            user.mobile_number,
            user.birthday.strftime('%d %B,%Y'),
            user.subjects,
            user.hobbies.value,
            file_name,
            user.current_address,
            f'{user.state} {user.city}',
        )
        self.close_form()


class ProfilePage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.user_email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')
        self.data_output = browser.element('#output')

    def open(self):
        browser.open('https://demoqa.com/text-box')
        return self

    def submit_form(self):
        self.submit.click()

    def fill_full_name(self, value: str):
        self.full_name.type(value)

    def fill_user_email(self, value: str):
        self.user_email.type(value)

    def fill_current_address(self, value: str):
        self.current_address.type(value)

    def fill_permanent_address(self, value: str):
        self.permanent_address.type(value)

    def check_registration_output(self, full_name, email, current_address, permanent_address):
        self.data_output.perform(command.js.scroll_into_view)
        self.data_output.element('#name').should(have.text(f"Name:{full_name}"))
        self.data_output.element('#email').should(have.text(f"Email:{email}"))
        self.data_output.element('#currentAddress').should(have.text(f"Current Address :{current_address}"))
        self.data_output.element('#permanentAddress').should(have.text(f"Permananet Address :{permanent_address}"))

    def register(self, user: User):
        self.fill_full_name(f'{user.first_name} {user.last_name}')
        self.fill_user_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        self.submit_form()

    def should_have_registered(self, user: User):
        self.check_registration_output(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.current_address,
            user.permanent_address
        )
