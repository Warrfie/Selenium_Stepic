from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_URL = "login"
    PROMO_URL = "?promo=newYear"

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    ADD_TO_CARD_LINK = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_FORM = (By.CSS_SELECTOR, "#content_inner")

    BOOK_NAME_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    BOOK_PRICE_NOTIFICATION = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")

class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    ITEMS_CONTAINER = (By.CSS_SELECTOR, "#basket_formset")
    NO_ITEMS_TEXT = (By.CSS_SELECTOR, "#content_inner")