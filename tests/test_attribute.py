from pages.text_box import TextBox


def test_placeholder(browser):
    text = TextBox(browser)
    text.visit()
    assert text.full_name.get_dom_attribute("placeholder") == "Full Name"
