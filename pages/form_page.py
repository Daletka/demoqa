from components.components import WebElements
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        super().__init__(driver, self.base_url)

        self.first_name = WebElements(driver, "#firstName")
        self.last_name = WebElements(driver, "#lastName")
        self.user_email = WebElements(driver, "#userEmail")
        self.gender_radio_1 = WebElements(driver, "#gender-radio-1")
        self.user_number = WebElements(driver, "#userNumber")
        self.btn_submit = WebElements(driver, "#submit")
        self.modal_dialog = WebElements(driver, "body > div.fade.modal.show > div")
        self.btn_close_modal = WebElements(driver, "#closeLargeModal")
        self.hobby_sport = WebElements(driver, "#hobbies-checkbox-1")
        self.hobby_read = WebElements(driver,"#hobbies-checkbox-2")
        self.hobby_music = WebElements(driver,"#hobbies-checkbox-3")
        self.address = WebElements(driver, "#currentAddress")
        self.state = WebElements(driver, "#state > div > div:nth-child(1) >div:nth-child(1)")
        self.user_form = WebElements(driver, "#userForm")
