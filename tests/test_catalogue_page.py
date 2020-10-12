from pages.catalogue_page import CataloguePage
from time import sleep


def test_user_can_add_random_available_item_to_basket(browser):
    # Arrange
    catalogue_page = CataloguePage(browser, CataloguePage.CATALOGUE_PAGE_LINK)
    catalogue_page.open()

    # Act
    catalogue_page.get_all_available_items()

