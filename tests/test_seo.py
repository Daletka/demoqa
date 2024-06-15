from pages.demoqa import DemoQa

def test_seo(browser):
    seo = DemoQa(browser)
    seo.visit()
    assert browser.title == "DEMOQA"