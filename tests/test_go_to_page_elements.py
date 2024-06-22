from pages.demoqa import DemoQa
from pages.elem_page import Elements
import time


def test_visit_element(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert el_page.equal_url()