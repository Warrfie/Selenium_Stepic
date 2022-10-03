import time

import pytest

from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


home_link = "http://selenium1py.pythonanywhere.com/"
new_year_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
another_item_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
password = "qwh123KJff"


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, home_link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", password)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, another_item_link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, another_item_link)
        page.open()
        page.should_be_authorized_user()
        page.should_be_product_page()
        page.add_to_card()
        page.solve_quiz_and_get_code()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.should_not_be_success_message()


def test_new_year_add_to_card(browser):
    page = ProductPage(browser, new_year_link)
    page.open()
    page.should_be_product_page(MainPageLocators.PROMO_URL)
    page.add_to_card()
    page.solve_quiz_and_get_code()


def test_universality(browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.should_be_product_page()
    page.get_product_price_and_name()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.compare_notifications_and_real()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.get_product_price_and_name()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.compare_notifications_and_real()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.should_disappeared_message()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, home_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_clear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, another_item_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_clear()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
