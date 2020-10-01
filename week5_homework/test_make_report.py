from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.random_credentials import random_string, random_email


def test_newly_registered_user_is_authorized(browser):
    # Arrange
    main_page = MainPage(browser, MainPage.MAIN_PAGE_LINK)
    main_page.open()
    main_page.go_to_login_page()

    # Act
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(random_email(6, 3, 2), random_string(10))

    # Assert
    login_page.should_be_authorized_user()
