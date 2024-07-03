import time
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal = ModalDialogs(browser)
    modal.visit()
    if browser.current_url == modal.base_url:
        assert modal.showSmallModal.exist()
        assert modal.showLargeModal.exist()
        modal.showLargeModal.click()
        assert modal.LargeModal
        modal.LargeModal_close.click()
        assert not modal.LargeModal.exist()
        modal.showSmallModal.click()
        assert modal.SmallModal.exist()
        modal.SmallModal_close.click()
        assert not modal.SmallModal.exist()
    else:
        browser.quit()
