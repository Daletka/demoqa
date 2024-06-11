import time
from pages.elem_page import Elements


def test_visible_btn_sidebar(browser):
    elem_vis_btn = Elements(browser)
    elem_vis_btn.visit()
#    elem_vis_btn.btn_sidebar_first.clck()
    time.sleep(2)
#    assert elem_vis_btn.btn_sidebar_first_text.exist()
    assert elem_vis_btn.btn_sidebar_first_text.visbl()


def test_not_visible_btn_sidebar(browser):
    elem_vis_btn = Elements(browser)
    elem_vis_btn.visit()
    assert elem_vis_btn.btn_sidebar_first_checkbox.visbl()
    elem_vis_btn.btn_sidebar_first.clck()
    time.sleep(2)
    assert not elem_vis_btn.btn_sidebar_first_checkbox.visbl()