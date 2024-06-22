import time
from pages.accordion import Accordion


def test_visible_accordion(browser):
    acc_vis_elem = Accordion(browser)
    acc_vis_elem.visit()
    assert acc_vis_elem.s_what.visibl()
    acc_vis_elem.s_what_head.click()
    time.sleep(2)
    assert not acc_vis_elem.s_what.visibl()


def test_visible_accordion_default(browser):
    acc_def_elem = Accordion(browser)
    acc_def_elem.visit()
    assert not acc_def_elem.s_where_text_first.visibl()
    assert not acc_def_elem.s_where_text_second.visibl()
    assert not acc_def_elem.s_why.visibl()
