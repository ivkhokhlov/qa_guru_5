from data.user import ivan
from model.pages.student_registration_form import RegistrationPage


def test_student_registration():
    registration_page = RegistrationPage()
    registration_page.register(user=ivan).submit()
    registration_page.should_have_registered(user=ivan)
