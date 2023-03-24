from .base_page import *
from .locators import *


class ProductPage(BasePage):
    def add_in_cart(self):
        cart_btn = self.driver.find_element(*ProductPageLocators.ADD_IN_CART)
        cart_btn.click()

    def should_be_same_price_book_and_cart(self):
        book_price = self.driver.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        cart_total = self.driver.find_element(*ProductPageLocators.TOTAL_OF_CART).text
        assert book_price in cart_total,'price is different'

    def should_be_success_message(self):
        assert self.driver.find_elements(*ProductPageLocators.ADD_MESSAGE), 'book not added to cart'

    def should_be_same_name_of_book(self):
        add_message = self.driver.find_element(*ProductPageLocators.ADD_MESSAGE).text
        book_name = self.driver.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        assert book_name in add_message, 'name is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE),"Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE),'Success message is not dissappeared'