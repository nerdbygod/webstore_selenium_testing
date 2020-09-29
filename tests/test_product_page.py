from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                  "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                  "?promo=offer6", pytest.param("?promo=offer7",
                                                                marks=pytest.mark.xfail(reason="won't fix")),
                                  "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # Arrange
    product_page_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Act
    item_title = product_page.item_title_text()
    item_price = product_page.item_price_text()
    product_page.add_to_cart()

    quiz_answer = ProductPage(browser, product_page_link)
    quiz_answer.solve_quiz_and_get_code()

    # Assert
    product_page.should_be_item_in_basket(item_title, item_price)
