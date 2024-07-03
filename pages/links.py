from components.components import WebElement
from pages.base_page import BasePage


class Links(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/links"
        super().__init__(driver, self.base_url)
        self.btn_home = WebElement(driver, "#simpleLink")
