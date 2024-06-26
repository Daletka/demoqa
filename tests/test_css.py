from pages.text_box import TextBox


def test_text_box_submint(browser):
    btn_check = TextBox(browser)
    btn_check.visit()
    assert btn_check.btn_submit.check_css("color", "rgba(255, 255, 255, 1)")
    assert btn_check.btn_submit.check_css("backgroundColor", "rgba(0, 123, 255, 1)")
    assert btn_check.btn_submit.check_css("borderColor", "rgba(0, 123, 255)")
