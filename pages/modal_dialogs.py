from components.components import WebElements
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)
        self.menu_button = WebElements(driver,"div:nth-child(3) > div > ul > li")
        self.icon = WebElements(driver, '#app > header > a')
