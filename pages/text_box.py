from components.components import WebElements
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)
        self.full_name = WebElements(driver, "#userName")
        self.mail = WebElements(driver, "#userEmail")
        self.address = WebElements(driver, "#currentAddress")
        self.perm_addres = WebElements(driver, "#permanentAddress")
        self.btn_submit = WebElements(driver, "#submit")
        self.last_name = WebElements(driver, "#output > div #name")
        self.last_addres = WebElements(driver, "#output > div #currentAddress")
