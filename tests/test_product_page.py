from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('offer_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                        "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                        "?promo=offer6", pytest.param("?promo=offer7",
                                                                      marks=pytest.mark.xfail(reason="won't fix")),
                                        "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer_link):
    # Arrange - product page link opening needs to be moved into ProductPage class
    # and offer link parameter is the only changing thing that must be called here
    product_page_link = f"{ProductPage.product_page_link}{offer_link}"
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Act
    item_title = product_page.get_item_title_as_text()
    item_price = product_page.get_item_price_as_text()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    # Assert
    product_page.verify_add_to_basket_notification(item_title, item_price)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Arrange
    product_page_link = ProductPage.product_page_link
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Act
    product_page.add_to_cart()

    # Assert
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Arrange
    product_page_link = ProductPage.product_page_link
    product_page = ProductPage(browser, product_page_link)

    # Act
    product_page.open()

    # Assert
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    # Arrange
    product_page_link = ProductPage.product_page_link
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Act
    product_page.add_to_cart()

    # Assert
    product_page.success_message_should_disappear()
