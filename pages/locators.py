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


class AddingItemsToTheCartLocators():
    ADDING_TO_THE_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_IN_THE_PAGE = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_IN_THE_CART = (By.CSS_SELECTOR, "div.alertinner > strong")
