from selene import browser
from selene import be, have
from random import choice


def test_submit_form_with_valid_data(browser_management, faker, tmp_path):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type(faker.first_name())
    browser.element('#lastName').should(be.blank).type(faker.last_name())
    browser.element('#userEmail').should(be.blank).type(faker.email())
    browser.element('#genterWrapper').element('[name="gender"]').double_click()
    browser.element('#userNumber').should(be.blank).type(faker.random_number(digits=10))

    browser.element('#dateOfBirthInput').click()
    choice(browser.all('.react-datepicker__day')).click()

    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()

    file = tmp_path / "file.jpg"
    file.write_bytes(faker.image())
    browser.element('#uploadPicture').send_keys(str(file))

    browser.element('#currentAddress').should(be.blank).type(faker.address())
    browser.element('//*[contains(text(),"Select State")]').click().element('//*[contains(text(),"NCR")]').click()
    browser.element('//*[contains(text(),"Select City")]').click().element('//*[contains(text(),"Delhi")]').click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))




