import time

from pages.webtables import Tables


def test_webtables(browser):
    webtables = Tables(browser)
    webtables.visit()
    assert webtables.btn_add.exist()
    webtables.btn_add.click()
    assert webtables.modal.exist()
    webtables.btn_submit.click()
    assert webtables.user_form.get_dom_attribute('class') == "was-validated"
    webtables.first_name.send_keys("Ivan")
    webtables.last_name.send_keys("Ivanov")
    webtables.email.send_keys('ivanov@example.com')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('50000')
    webtables.depart.send_keys("Legal")
    webtables.btn_submit.click()
    assert not webtables.modal.exist()
    assert webtables.new_row.exist()
    webtables.btn_edit.click()
    assert webtables.modal.exist()
    webtables.first_name.clear()
    webtables.first_name.send_keys("Test")
    webtables.btn_submit.click()
    assert webtables.new_name.exist()
    webtables.btn_del.click()
    assert not webtables.new_name.exist()

def test_next_previous(browser):
    webtables = Tables(browser)
    webtables.visit()
    webtables.row.click()
    time.sleep(2)
    webtables.btn_5_row.click()
    webtables.btn_next.click_force()
    assert webtables.page_of.get_text() == '1'
    webtables.btn_prev.click_force()
    assert webtables.page_of.get_text() == '1'
    assert webtables.btn_next.get_dom_attribute("disabled")
    time.sleep(2)
    for i in range(3):
        webtables.btn_add.click()
        webtables.first_name.send_keys("Ivan")
        webtables.last_name.send_keys("Ivanov")
        webtables.email.send_keys('ivanov@example.com')
        webtables.age.send_keys('30')
        webtables.salary.send_keys('50000')
        webtables.depart.send_keys("Legal")
        webtables.btn_submit.click()
    time.sleep(3)
    assert webtables.page_of.get_text() == '2'
    webtables.btn_next.click()
    assert webtables.page.get_dom_attribute("value") == '2'
    time.sleep(2)
    webtables.btn_prev.click()
    assert webtables.page.get_dom_attribute("value") == '1'
