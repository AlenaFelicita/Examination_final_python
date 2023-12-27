from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class TestLocators:
    locs = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)

    for i in locators['xpath'].keys():
        locs[i] = (By.XPATH, locators['xpath'][i])

    for i in locators['css'].keys():
        locs[i] = (By.CSS_SELECTOR, locators['css'][i])


class Operations(BasePage, TestLocators):


    def enter_bad_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.locs['login'])
        if input1:
            input1.send_keys(testdata['bad_username'])
        else:
            logging.error('Enter login field is not found')

    def enter_bad_password(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.locs['password'])
        if input2:
            input2.send_keys(testdata['bad_username'])
        else:
            logging.error('Enter password field is not found')

    def enter_good_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.locs['login'])
        if input1:
            input1.send_keys(testdata['username'])
        else:
            logging.error('Enter login field is not found')

    def enter_good_password(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.locs['password'])
        if input2:
            input2.send_keys(testdata['password'])
        else:
            logging.error('Enter password field is not found')

    def enter_name(self):
        logging.info('Enter name ')
        name_field = self.find_element(self.locs['name_field'])
        if name_field:
            name_field.send_keys(testdata['contact_us']['name'])
        else:
            logging.error('Enter name field is not found')

    def enter_email(self):
        logging.info('Enter email ')
        email_field = self.find_element(self.locs['email_field'])
        if email_field:
            email_field.send_keys(testdata['contact_us']['email'])
        else:
            logging.error('Enter email field is not found')

    def enter_content(self):
        logging.info('Enter content ')
        content_field = self.find_element(self.locs['content_field'])
        if content_field:
            content_field.send_keys(testdata['contact_us']['content'])
        else:
            logging.error('Enter email field is not found')


    def click_login_button(self):
        logging.info('Click login button ')
        btn = self.find_element(self.locs['btn_selector'])
        if btn:
            btn.click()
            time.sleep(3)
        else:
            logging.error('Login button is not found')

    def click_contact_button(self):
        logging.info('Click contact button ')
        cont_btn = self.find_element(self.locs['contact_btn'])
        if cont_btn:
            cont_btn.click()
            time.sleep(3)
        else:
            logging.error('Contact button is not found')

    def click_contact_us_button(self):
        logging.info('Click contact us button ')
        cont_us_btn = self.find_element(self.locs['contact_us_btn'])
        if cont_us_btn:
            cont_us_btn.click()
            time.sleep(3)
        else:
            logging.error('Contact us button is not found')

    def click_about_button(self):
        logging.info('Click "About" button')
        about_btn = self.find_element(self.locs['about_btn'])
        if about_btn:
            about_btn.click()
            time.sleep(3)
        else:
            logging.error('"About" button is not found')


    def get_error_text(self):
        err_label = self.find_element(self.locs['err_label'])
        if err_label:
            text = err_label.text
            logging.info(f'Error {text} while loging')
            return text
        else:
            logging.error(f'Element with error text is not found')
            return None

    def get_hello_user(self):
        hello = self.find_element(self.locs['hello_user'])
        if hello:
            text = hello.text
            logging.info(text)
            return text
        else:
            logging.error('"Hello, User" element is not found')
            return None

    def switch_alert(self):
        logging.info('Switch alert')
        text = self.alert()
        logging.info(text)
        return text

    def get_about_page_text(self):
        about_page = self.find_element(self.locs['about_page_title'])
        if about_page:
            text = about_page.text
            logging.info('About Page is loaded, title is visible')
        else:
            logging.error('About Page title is not visible')
            text = None
        return text

    def check_about_page_title_font_size(self, right_font_size):
        title = self.find_element(self.locs['about_page_title'])
        font_size = title.value_of_css_property('font-size')
        if font_size == right_font_size:
            logging.info(f'About Page title has {font_size} font size')
            return True
        else:
            logging.error(f'Font size of title "About" Page is not equal to {right_font_size}')
            return False
