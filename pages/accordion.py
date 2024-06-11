from components.components import WebElements
from pages.base_page import BasePage


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)
        self.s_what = WebElements(driver, "#section1Content > p")
        self.s_what_head = WebElements(driver, "#section1Heading")
        self.s_where_text_first = WebElements(driver, "#section2Content > p:nth-child(1)")
        self.s_where_text_second = WebElements(driver, "#section2Content > p:nth-child(2)")
        self.s_why = WebElements(driver, "#section3Content > p")

