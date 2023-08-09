from selene import browser
from selene import be, have
from random import choice
import os


def test_submit_form_with_valid_data(browser_management, faker):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Khokhlov')
    browser.element('#userEmail').should(be.blank).type('ivan@example.com')
    browser.element('#genterWrapper').element('[name="gender"]').double_click()
    browser.element('#userNumber').should(be.blank).type('0123456789')


    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1993"]').click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/img.jpeg'))
    browser.element('#currentAddress').should(be.blank).type('г. Магадан, ул. Ленина 21-72')
    browser.element('//*[contains(text(),"Select State")]').click().element('//*[contains(text(),"NCR")]').click()
    browser.element('//*[contains(text(),"Select City")]').click().element('//*[contains(text(),"Delhi")]').click()

    browser.element('#submit').submit()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Ivan Khokhlov'
                                               and 'ivan@example.com'
                                               and '0123456789'
                                               and '15 September,1993'
                                               and 'г. Магадан, ул. Ленина 21-72'
                                               and 'Maths'
                                               and 'NCR'
                                               and 'Delhi'))




