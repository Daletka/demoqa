from pages.links import Links


def test_window_tab(browser):
    link = Links(browser)
    link.visit()
    assert link.btn_home.exist()
    assert link.btn_home.get_text() == "Home"
    assert link.btn_home.get_dom_attribute('href') == "https://demoqa.com"
    link.btn_home.click()
    assert len(browser.window_handles) == 2