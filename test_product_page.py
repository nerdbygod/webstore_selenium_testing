from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # Arrange
    product_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/reversing_202/"
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
