from conftest import browser
from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        go_to_login_form = self.browser.find_element(*LoginPageLocators.GO_TO_LOGIN_PAGE_BUTTON)
        go_to_login_form.click()
        assert self.browser.current_url == 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'

    def should_be_login_form(self):
        go_to_login_form_button = self.browser.find_element(*LoginPageLocators.GO_TO_LOGIN_PAGE_BUTTON)
        go_to_login_form_button.click()
        log_in_form_box = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BOX)
        assert log_in_form_box.text == 'Войти'

    def should_be_register_form(self):
        go_to_login_form_button = self.browser.find_element(*LoginPageLocators.GO_TO_LOGIN_PAGE_BUTTON)
        go_to_login_form_button.click()
        registration_form_box = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BOX)
        assert registration_form_box.text == 'Зарегистрироваться'
