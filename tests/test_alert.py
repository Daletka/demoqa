import time
from pages.alerts import Alerts
def tst_allert(browser):
    page_alert = Alerts(browser)
    page_alert.visit()
    assert not page_alert.alert()
    page_alert.btn_alert.click()
    time.sleep(2)
    assert page_alert.alert()
    page_alert.alert().accept()


def tst_alert_text(browser):
    page_allert = Alerts(browser)
    page_allert.visit()
    page_allert.btn_alert.click()
    time.sleep(2)
    assert page_allert.alert().text == 'You clicked a button'
    page_allert.alert().accept()
    assert not page_allert.alert()
    time.sleep(2)


def tst_confirm(browser):
    page_confirm = Alerts(browser)
    page_confirm.visit()
    page_confirm.btn_confirm.click()
    time.sleep(2)
    page_confirm.alert().dismiss()
    assert page_confirm.txt_confirm.get_text() == 'You selected Cancel'


def tst_promt(browser):
    page_promt = Alerts(browser)
    page_promt.visit()
    name = "Irina"
    page_promt.btn_promt.click()
    time.sleep(2)
    page_promt.alert().send_keys(name)
    page_promt.alert().accept()
    assert page_promt.txt_promt.get_text() == f"You entered {name}"
    time.sleep(2)
