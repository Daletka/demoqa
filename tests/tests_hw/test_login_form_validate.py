import time

from pages.form_page import FormPage


def test_login_form_validate(browser):
    login = FormPage(browser)
    login.visit()
    assert login.first_name.get_dom_attribute("placeholder") == "First Name"
    assert login.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert login.user_email.get_dom_attribute("placeholder") == "name@example.com"
    assert login.user_email.get_dom_attribute("pattern") == r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    time.sleep(2)
    login.btn_submit.clck_force()
    time.sleep(3)
    assert login.user_form.get_dom_attribute("class") == "was-validated"
