from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_clear(self):
        self.should_be_no_items()
        self.should_be_clear_text()

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_CONTAINER), "Card is not empty"

    def should_be_clear_text(self):
        assert self.browser.find_element(*BasketPageLocators.NO_ITEMS_TEXT).text == "Your basket is empty. Continue shopping", "No 'Basket empty' text"


