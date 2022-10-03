import math

from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    product_price = None
    product_name = None

    def should_be_product_page(self, promo=None):
        self.should_be_promo_url(promo)
        self.should_be_product_form()
        self.should_be_add_to_card_button()

    def should_be_promo_url(self, promo):
        if promo is not None:
            assert promo in self.browser.current_url, "No '?promo=newYear' in url"

    def should_be_product_form(self):
        assert self.is_element_present(*MainPageLocators.PRODUCT_FORM), "Product form is not presented"

    def should_be_add_to_card_button(self):
        assert self.is_element_present(*MainPageLocators.ADD_TO_CARD_LINK), "Add to card url is not presented"

    def add_to_card(self):
        link = self.browser.find_element(*MainPageLocators.ADD_TO_CARD_LINK)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_price_and_name(self):
        self.product_price = self.browser.find_element(*MainPageLocators.BOOK_PRICE).text
        self.product_name = self.browser.find_element(*MainPageLocators.BOOK_NAME).text

    def compare_notifications_and_real(self):
        assert self.product_price == self.browser.find_element(*MainPageLocators.BOOK_PRICE_NOTIFICATION).text, "Real price and cart price not equal"
        assert self.product_name == self.browser.find_element(*MainPageLocators.BOOK_NAME_NOTIFICATION).text, "Real name and notification name not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"