from components.components import WebElements
from pages.base_page import BasePage


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)
        self.icon = WebElements(driver, '#app > header > a')
        self.btn_elements = WebElements(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElements(driver, "#app > footer > span")
        self.title = WebElements(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6")
