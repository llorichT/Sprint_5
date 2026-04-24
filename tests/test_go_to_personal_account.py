from helpers.waits import wait_for_visible, safe_click, wait_overlay_disappear
from pages.locators import MainPageLocators, LoginPageLocators
from url import BASE_URL


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        try:
            driver.get(BASE_URL)

            wait_overlay_disappear(driver)
            safe_click(driver, MainPageLocators.PERSONAL_ACCOUNT)

            email_input = wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)

            assert email_input.is_displayed()

        finally:
            driver.quit()
