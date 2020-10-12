from pages.base_page import BasePage
from .locators import MainPageLocators, CataloguePageLocators


class CataloguePage(BasePage):
    CATALOGUE_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/"

    def go_to_main_page(self):
        self.browser.find_element(*CataloguePageLocators.BACK_TO_MAIN_PAGE_LINK_NAV).click()

    def switch_to_books_category(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_BOOKS_BUTTON).click()
        assert "books_2" in self.browser.current_url, \
            "Should be books category in browser url"

    def switch_to_clothing_category(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_CLOTHING_BUTTON).click()
        assert "clothing_1" in self.browser.current_url, \
            "Should be clothing category in browser url"

    # https://stackoverflow.com/questions/64326135/how-do-i-properly-iterate-through-a-list-of-web-elements-in-selenium-webdriver-u
    def get_all_available_items(self):
        all_items_on_page = self.browser.find_elements(*CataloguePageLocators.PRODUCT_POD_ARTICLE)
        print(f"Total number of items on page is {len(all_items_on_page)}")
        available_items = []
        for item in all_items_on_page:
            if self.is_element_present(*CataloguePageLocators.AVAILABLE_ITEM_TAG):
                available_items.append(item)
        print(f"Total number of available items is {len(available_items)}")
        return available_items
