from pages.webtables import Tables


def test_webtables(browser):
    webtables = Tables(browser)
    webtables.visit()
    assert not webtables.no_row.exist()
    assert not webtables.btn_del.check_count_elements(0)

    while webtables.btn_del.exist():
        webtables.btn_del.click()

    assert webtables.no_row.exist()
