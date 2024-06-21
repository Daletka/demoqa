import time
from pages.form_page import FormPage


def tst_login_form(browser):
    form_page = FormPage(browser)
    
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    #time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.clck_force()
    form_page.user_number.send_keys("1234567890")
    form_page.hobby_read.clck_force()
    form_page.address.send_keys("aaa aa aaa")
    #time.sleep(2)
    form_page.btn_submit.clck_force()
    #time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.clck_force()
    #time.sleep(3)


def test_click(browser):
    form = FormPage(browser)
    form.state.scroll_to_element()
    #form.state.clck_force()
    time.sleep(3)
