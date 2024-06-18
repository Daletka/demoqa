import time
from pages.text_box import TextBox


def test_clear(browser):
    text = TextBox(browser)
    text.visit()
    text.full_name.send_keys("Aaa Aaa")
    time.sleep(2)
    text.full_name.clear()
    time.sleep(2)
    assert text.full_name.get_text() == ""
