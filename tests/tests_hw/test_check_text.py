from pages.demoqa import DemoQa


def test_check_footer(browser):
    ft_page = DemoQa(browser)

    ft_page.visit()
    assert ft_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_title(browser):
    elem_page = DemoQa(browser)
    elem_page.visit()
    elem_page.btn_elements.clck()
    assert elem_page.title.get_text() == 'Please select an item from left to start practice.'
