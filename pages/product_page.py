from .base_page import BasePage
from .locators import AddingItemsToTheCartLocators


class ProductPage(BasePage):
    def adding_item_to_cart(self):
        button = self.browser.find_element(*AddingItemsToTheCartLocators.ADDING_TO_THE_CART_BUTTON)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    def user_on_the_product_page(self):
        self.same_name_of_product_in_page_and_in_cart()
        self.same_price_of_product_in_page_and_in_cart()

    def same_name_of_product_in_page_and_in_cart(self):
        product_name_page = self.browser.find_element(*AddingItemsToTheCartLocators.PRODUCT_NAME_IN_THE_PAGE).text
        product_name_basket = self.browser.find_element(*AddingItemsToTheCartLocators.PRODUCT_NAME_IN_THE_CART).text
        assert product_name_basket == product_name_page, \
            f"Product names are different! {product_name_page} != {product_name_basket}"

    def same_price_of_product_in_page_and_in_cart(self):
        product_price = self.browser.find_element(*AddingItemsToTheCartLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*AddingItemsToTheCartLocators.CART_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices are different! {product_price} != {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddingItemsToTheCartLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but shouldn't be"

    def should_see_as_disappearing_message(self):
        assert self.is_disappeared(*AddingItemsToTheCartLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but could be disappeared"
