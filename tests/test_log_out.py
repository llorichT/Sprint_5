from url import BASE_URL
from pages.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers.auth import register_generated_user, login
from helpers.waits import wait_for_visible, safe_click, wait_overlay_disappear


class TestLogout:

    def test_logout(self, driver):
        user = register_generated_user(driver)

        driver.get(BASE_URL)
        safe_click(driver, MainPageLocators.LOGIN_BUTTON)

        login(driver, user["email"], user["password"])

        wait_overlay_disappear(driver)

        safe_click(driver, MainPageLocators.PERSONAL_ACCOUNT)
        safe_click(driver, ProfilePageLocators.LOGOUT_BUTTON)

        login_form = wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)

        assert login_form.is_displayed()