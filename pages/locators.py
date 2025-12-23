from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    GO_TO_LOGIN_PAGE_BUTTON = (By.ID, 'login_link')
    LOGIN_FORM_BOX = (By.ID, 'login_form')
    LOGIN_FORM_EMAIL_INPUT = (By.NAME, 'login-username')
    LOGIN_FORM_PASSWORD_INPUT = (By.NAME, 'login-password')
    LOGIN_FORM_BUTTON_SUBMIT = (By.NAME, 'login_submit')
    REGISTRATION_FORM_BOX = (By.ID, 'register_form')
    REGISTRATION_EMAIL_INPUT = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD_INPUT = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_REPEAT_INPUT = (By.NAME, 'registration-password2')
    REGISTRATION_FORM_SUBMIT = (By.NAME, 'registration_submit')
