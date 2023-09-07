from selene import have
from selene.support.shared import browser

from data.user import User


class RegistrationPage:

    def __init__(self):
        pass

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self, gender):
        browser.element('#genterWrapper').element(f'[value="{gender}"]').double_click()

    def fill_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_date_of_birth(self, day: str, month: str, year: str):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select [value="{int(month)}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
        browser.element(f'.react-datepicker__day--{day.zfill(3)}').click()

    def fill_subjects(self, *subjects):
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_enter()

    def choose_hobbies(self, *hobbies):
        for hobby in hobbies:
            browser.element('#hobbiesWrapper').element(f'//*[contains(text(),"{hobby}")]').click()

    def upload_picture(self, path_to_img):
        browser.element('#uploadPicture').send_keys(path_to_img)
        pass

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        pass

    def fill_state(self, state):
        browser.element('//*[contains(text(),"Select State")]').click().element(
            f'//*[contains(text(),"{state}")]'
        ).click()
        pass

    def fill_city(self, city):
        browser.element('//*[contains(text(),"Select City")]').click().element(
            f'//*[contains(text(),"{city}")]'
        ).click()
        pass

    def submit(self):
        browser.element('#submit').submit()
        pass

    def should_have_registered(self, user: User):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.element('.table').should(have.text(f'{user.first_name} {user.last_name}'
                                                   and user.email
                                                   and user.gender
                                                   and user.mobile
                                                   and ', '.join(user.subjects)
                                                   and ', '.join(user.hobbies)
                                                   and user.address
                                                   and user.state
                                                   and user.city))

    def register(self, user: User):
        self.open()
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_number(user.mobile)
        self.fill_date_of_birth(user.day, user.month, user.year)
        self.fill_subjects(*user.subjects)
        self.choose_hobbies(*user.hobbies)
        self.upload_picture(user.image)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        return self
