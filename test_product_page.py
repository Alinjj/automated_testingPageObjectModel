import time
import pytest
from .pages.product_page import *
from .pages.basket_page import BasketPage
from .pages.login_page import *


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(driver,link):
    page = ProductPage(driver,link)
    page.open()
    page.add_in_cart()
    page.should_be_same_price_book_and_cart()
    page.should_be_same_name_of_book()
    page.should_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver,link)
    page.open()
    page.add_in_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver,link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver,link)
    page.open()
    page.add_in_cart()
    page.success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver,link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver,link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver,driver.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,driver):
        page = LoginPage(driver,link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,driver):
        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,driver):
        page = ProductPage(driver, link)
        page.open()
        page.add_in_cart()
        page.should_be_same_price_book_and_cart()
        page.should_be_same_name_of_book()
        page.should_be_success_message()

