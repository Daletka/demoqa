import time
import pytest

from pages.accordion import Accordion
from pages.demoqa import DemoQa
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

def test_seo(browser):
    seo = DemoQa(browser)
    seo.visit()
    assert browser.title == "DEMOQA"


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
