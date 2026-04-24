from helpers.auth import register_generated_user, login
from helpers.waits import wait_for_visible, safe_click
from pages.locators import (
    MainPageLocators,
    RegisterPageLocators,
    LoginPageLocators,
    ForgotPasswordPageLocators,
)
from url import BASE_URL, REGISTER_URL, LOGIN_URL


class TestLogin:

    def test_login_from_main_button(self, driver):
        try:
            user = register_generated_user(driver)

            driver.get(BASE_URL)
            safe_click(driver, MainPageLocators.LOGIN_BUTTON)

            login(driver, user["email"], user["password"])

            assert wait_for_visible(driver, MainPageLocators.PERSONAL_ACCOUNT).is_displayed()

        finally:
            driver.quit()

    def test_login_from_personal_account(self, driver):
        try:
            user = register_generated_user(driver)

            driver.get(BASE_URL)
            safe_click(driver, MainPageLocators.PERSONAL_ACCOUNT)

            login(driver, user["email"], user["password"])

            assert wait_for_visible(driver, MainPageLocators.PERSONAL_ACCOUNT).is_displayed()

        finally:
            driver.quit()

    def test_login_from_register_form(self, driver):
        try:
            user = register_generated_user(driver)

            driver.get(REGISTER_URL)
            safe_click(driver, RegisterPageLocators.LOGIN_LINK)

            login(driver, user["email"], user["password"])

            assert wait_for_visible(driver, MainPageLocators.PERSONAL_ACCOUNT).is_displayed()

        finally:
            driver.quit()

    def test_login_from_forgot_password_form(self, driver):
        try:
            user = register_generated_user(driver)

            driver.get(LOGIN_URL)
            safe_click(driver, LoginPageLocators.FORGOT_PASSWORD_LINK)
            safe_click(driver, ForgotPasswordPageLocators.LOGIN_LINK)

            login(driver, user["email"], user["password"])

            assert wait_for_visible(driver, MainPageLocators.PERSONAL_ACCOUNT).is_displayed()

        finally:
            driver.quit()