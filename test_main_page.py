import time

import pytest

from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from .pages.main_page import MainPage

home_link = "http://selenium1py.pythonanywhere.com/"
new_year_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
another_item_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, home_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, home_link)
    page.open()
    #login_page = page.go_to_login_page()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

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


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
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