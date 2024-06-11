from pages.demoqa import DemoQa
from pages.elem_page import Elements


def tst_check_footer(browser):
    ft_page = DemoQa(browser)

    ft_page.visit()
    assert ft_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def tst_check_title(browser):
    elem_page = DemoQa(browser)
    elem_page.visit()
    elem_page.btn_elements.clck()
    assert elem_page.title.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elem_text = Elements(browser)
    elem_text.visit()

    assert elem_text.text_elem.get_text() == 'Elements'
    assert elem_text.icon_e.exist()
    assert elem_text.btn_sidebar_first.exist()
    assert elem_text.btn_sidebar_first_text.exist()
