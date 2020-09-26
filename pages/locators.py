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
