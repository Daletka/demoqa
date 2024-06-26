from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)
        self.full_name = WebElement(driver, "#userName")
        self.mail = WebElement(driver, "#userEmail")
        self.address = WebElement(driver, "#currentAddress")
        self.perm_addres = WebElement(driver, "#permanentAddress")
        self.btn_submit = WebElement(driver, "#submit")
        self.last_name = WebElement(driver, "#output > div #name")
        self.last_addres = WebElement(driver, "#output > div #currentAddress")
