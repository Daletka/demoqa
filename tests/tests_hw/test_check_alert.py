import time
from pages.alerts import Alerts


def test_check_alert(browser):
    page_alert = Alerts(browser)
    page_alert.visit()
    assert page_alert.timerAlertButton.exist()
    page_alert.timerAlertButton.click()
    assert not page_alert.alert()
    time.sleep(5)
    assert page_alert.alert()
