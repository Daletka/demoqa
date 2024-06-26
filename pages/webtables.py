from components.components import WebElement
from pages.base_page import BasePage


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)
        self.no_row = WebElement(driver, "div.rt-noData")
        self.btn_del = WebElement(driver, "[title*='Delete']")
        self.btn_add = WebElement(driver, "#addNewRecordButton")
        self.modal = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.user_form = WebElement(driver, "#userForm")
        self.btn_submit = WebElement(driver, "#submit")
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.email = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, "#age")
        self.salary = WebElement(driver, "#salary")
        self.depart = WebElement(driver, "#department")
        self.btn_edit = WebElement(driver, "[title*='Edit']")
        self.page_of = WebElement(driver, "span.-pageInfo > span")
        self.page = WebElement(driver, "span.-pageInfo > div > input")
        self.l_first_name = WebElement(driver, "div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)")
        self.btn_prev = WebElement(driver, "div.-previous button.-btn")
        self.btn_next = WebElement(driver, "div.-next button.-btn")
        self.fourth_row = WebElement(driver,"div.rt-tbody > div:nth-child(4)")
        self.new_row = WebElement(driver, "//*[contains(text(), 'Ivan')]", 'xpath')
        self.new_name = WebElement(driver, "//*[contains(text(), 'Test')]", 'xpath')
        self.btn_5_row = WebElement(driver, "//*[contains(text(), '5 rows')]", 'xpath')
        self.row = WebElement(driver, "span.select-wrap.-pageSizeOptions > select")
