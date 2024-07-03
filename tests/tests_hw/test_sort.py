import time
from pages.webtables import Tables


def test_sort(browser):
    webtables = Tables(browser)
    webtables.visit()
    webtables.headFirstName.click()
    assert webtables.headFirstName.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
    webtables.headLastName.click()
    assert webtables.headLastName.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"

    webtables.headAge.click()
    assert webtables.headAge.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
    webtables.headEmail.click()
    assert webtables.headEmail.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
    webtables.headSalary.click()
    assert webtables.headSalary.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
    webtables.headDepartment.click()
    assert webtables.headDepartment.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
    webtables.headAction.click()
    assert webtables.headAction.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
