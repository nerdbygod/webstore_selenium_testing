import pytest
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from tests.random_credentials import random_string, random_email

# offer_link parameter should be refactored so that it doesn't need to be called
# for every ProductPage class object. Refer to product_page.py, line 8.


@pytest.mark.parametrize('offer_link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                        "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                        "?promo=offer6", pytest.param("?promo=offer7",
                                                                      marks=pytest.mark.xfail(reason="won't fix")),
                                        "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer_link):
    # Arrange
    product_page = ProductPage(browser, offer_link)
    product_page.open()

    # Act
    item_title = product_page.get_item_title_as_text()
    item_price = product_page.get_item_price_as_text()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    # Assert
    product_page.verify_add_to_basket_notification(item_title, item_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Arrange
    product_page = ProductPage(browser, offer_link="")
    product_page.open()

    # Act
    product_page.add_to_cart()

    # Assert
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Arrange
    product_page = ProductPage(browser, offer_link="")

    # Act
    product_page.open()

    # Assert
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Arrange
    product_page = ProductPage(browser, offer_link="")
    product_page.open()

    # Act
    product_page.add_to_cart()

    # Assert
    product_page.success_message_should_disappear()


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, ProductPage.product_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(random_email(7, 4, 3), random_string(10))
    login_page.should_be_authorized_user()


class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser, offer_link="")

        # Act
        product_page.open()

        # Assert
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, offer_link="")
        product_page.open()

        # Act
        item_title = product_page.get_item_title_as_text()
        item_price = product_page.get_item_price_as_text()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()

        # Assert
        product_page.verify_add_to_basket_notification(item_title, item_price)
