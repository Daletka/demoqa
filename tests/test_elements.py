from pages.elem_page import Elements


def test_find_elements(browser):
    elems = Elements(browser)
    elems.visit()
    assert elems.btns_first_menu.check_count_elements(9)
