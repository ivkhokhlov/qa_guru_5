import os
import allure
from model.pages.student_registration_form import RegistrationPage
from conftest import RESOURCES_DIR


@allure.title("Successful fill form")
def test_student_registration(browser_management):
    registration_page = RegistrationPage()

    with allure.step('Open registration form'):
        registration_page.open()

    with allure.step('Fill form'):
        registration_page.fill_first_name('Ivan')
        registration_page.fill_last_name('Khokhlov')
        registration_page.fill_email('ivan@example.com')
        registration_page.choose_gender('Male')
        registration_page.fill_number('0123456789')
        registration_page.fill_date_of_birth('07', '08', '2023')
        registration_page.fill_subjects('Math', 'Commerce')
        registration_page.choose_hobbies('Reading', 'Music')
        registration_page.upload_picture(os.path.join(RESOURCES_DIR, 'img.jpeg'))
        registration_page.fill_address('г. Магадан, ул. Ленина 21-72')
        registration_page.fill_state('NCR')
        registration_page.fill_city('Delhi')

    with allure.step('Submit form'):
        registration_page.submit()

    with allure.step('Check form submission'):
        registration_page.should_have_registered(
            full_name='Ivan Khokhlov',
            email='ivan@example.com',
            gender='Male',
            mobile='0123456789',
            birthday='07 September,2023',
            subjects=['Math', 'Commerce'],
            hobbies=['Reading', 'Music'],
            address='г. Магадан, ул. Ленина 21-72',
            state='NCR',
            city='Delhi'
        )

