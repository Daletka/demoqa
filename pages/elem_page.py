from components.components import WebElement
from pages.base_page import BasePage


class Elements(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_elem = WebElement(driver, "div:nth-child(1) > span > div > div.header-text")
        self.icon_e = WebElement(driver, "header > a > img")
        self.btn_sidebar_first = WebElement(driver, "div:nth-child(1) > span > div")
        self.btn_sidebar_first_text = WebElement(driver, "div:nth-child(1) > div > ul > #item-0 > span")
        self.btn_sidebar_first_checkbox = WebElement(driver, "div:nth-child(1) > div > ul > #item-1 > span")
        self.btns_first_menu = WebElement(driver, "div:nth-child(1) > div > ul > li")
