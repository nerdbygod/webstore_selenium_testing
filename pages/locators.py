from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE_URL = "accounts/login/"
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "#id_registration-email_invalid")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1_invalid")
    SIGNUP_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2_invalid")
    SIGNUP_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']_invalid")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username_invalid")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password_invalid")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']_invalid")


class ProductPageLocators():
    PROMO_ITEM_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PROMO_ITEM_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PROMO_ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    BASKET_PRICE_NOTIFICATION = By.CSS_SELECTOR, "#messages > div:last-child .alertinner strong"