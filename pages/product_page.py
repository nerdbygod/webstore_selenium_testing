from .main_page import MainPage
from .locators import ProductPageLocators


class ProductPage(MainPage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def item_price_text(self):
        item_price = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_PRICE)
        return item_price.text

    def item_title_text(self):
        item_title = self.browser.find_element(*ProductPageLocators.PROMO_ITEM_TITLE)
        return item_title.text

    def should_be_item_in_basket(self, item_title_text, item_price_text):
        item_in_basket_title_notif = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        item_in_basket_price_notif = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_NOTIFICATION)
        assert item_title_text == item_in_basket_title_notif.text, \
            "Item title should be correctly displayed in the basket"
        assert item_price_text in item_in_basket_price_notif.text, \
            "Item price should be correctly displayed in the basket"
