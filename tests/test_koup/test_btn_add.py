from pages.add_remove import KoupAdd
from pages.herokuapp import Koup


def test_btn_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()
    assert koup_page.link.find_element()
    koup_page.link.click()
    assert koup_add.equal_url()
    assert koup_add.btn_add.get_text() == "Add Element"
    assert koup_add.btn_add.get_dom_attribute("onclick") == "addElement()"
    for i in range(4):
        koup_add.btn_add.click()
    assert koup_add.btn_delete.check_count_elements(4)
    for element in koup_add.btn_delete.find_elements():
        assert element.text == "Delete"
    while koup_add.btn_delete.exist():
        koup_add.btn_delete.click()
    assert koup_add.btn_delete.check_count_elements(0)
