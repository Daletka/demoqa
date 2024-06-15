import time
from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal = ModalDialogs(browser)
    modal.visit()
    assert modal.menu_button.check_count_elements(5)


def test_navigation_modal(browser):
    modal = ModalDialogs(browser)
    main = DemoQa(browser)
    modal.visit()
    modal.refresh()

    time.sleep(2)

    modal.icon.clck()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    assert main.equal_url()
    assert browser.title == "DEMOQA"
    browser.set_window_size(1000, 1000)
    time.sleep(2)