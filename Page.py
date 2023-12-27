from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


with open("locators.yaml") as f:
    locators = yaml.safe_load(f)

with open("testdata.yaml") as f2:
    test_data = yaml.safe_load(f2)


class TestSearchLocators:
    locators_dict = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        locators_dict[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        locators_dict[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    # Methods user authorization
    def enter_login(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.locators_dict['LOCATOR_INPUT_LOGIN']}")
        login_field = self.find_element(TestSearchLocators.locators_dict['LOCATOR_INPUT_LOGIN'])
        if login_field:
            login_field.clear()
            login_field.send_keys(word)
        else:
            logging.error('Field Login not found')

    def enter_pass(self, word):
        logging.debug(f"Send {word} to element {TestSearchLocators.locators_dict['LOCATOR_INPUT_PASSWORD']}")
        password_field = self.find_element(TestSearchLocators.locators_dict['LOCATOR_INPUT_PASSWORD'])
        if password_field:
            password_field.clear()
            password_field.send_keys(word)
        else:
            logging.error('Field Password not found')

    # Methods button pressing
    def press_login_button(self):
        logging.debug("Click login button")
        btn = self.find_element(TestSearchLocators.locators_dict['LOCATOR_BTN_LOGIN'])
        if btn:
            btn.click()
        else:
            logging.error('Button Login not found')

    def press_about_btn(self):
        logging.debug("Click about link")
        btn = self.find_element(TestSearchLocators.locators_dict['LOCATOR_BTN_ABOUT'])
        if btn:
            btn.click()
        else:
            logging.error('Error click about link')

    # Methods for get text
    def get_title_about(self):
        about_page_field = self.find_element(TestSearchLocators.locators_dict['LOCATOR_TITLE_ABOUT_PAGE'], time=3)
        if about_page_field:
            font = about_page_field.value_of_css_property('font-size')
            logging.debug(f"We find '{font}' "
                          f"in error field {TestSearchLocators.locators_dict['LOCATOR_TITLE_ABOUT_PAGE']}")
            return font
        else:
            logging.error('Error header about page not found')
            return None
