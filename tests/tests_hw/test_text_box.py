from pages.text_box import TextBox

name = "test"
address = "test test"


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.full_name.send_keys(name)
    text_box.address.send_keys(address)
    text_box.btn_submit.click_force()
    assert text_box.last_name.get_text() == "Name:"+name
    assert text_box.last_addres.get_text() == "Current Address :" + address
