from testpage import BasePage
from testpage import Operations


def test_authorization_with_right_login(browser, hello_user):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    assert page.get_hello_user() == hello_user, \
        'User is not authorized'


def test_page_loading(browser, about_page):
    page = Operations(browser)
    page.click_about_button()
    assert page.get_about_page_text() == about_page, \
        'About page is not loaded'


def test_font_size(browser, font_size):
    page = Operations(browser)
    assert page.check_about_page_title_font_size(font_size), \
        f'About Page title font size is not equal to {font_size}'
