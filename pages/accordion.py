from components.components import WebElement
from pages.base_page import BasePage


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)
        self.s_what = WebElement(driver, "#section1Content > p")
        self.s_what_head = WebElement(driver, "#section1Heading")
        self.s_where_text_first = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.s_where_text_second = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.s_why = WebElement(driver, "#section3Content > p")

