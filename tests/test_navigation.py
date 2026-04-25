from helpers.waits import wait_for_clickable, wait_for_visible
from pages.locators import MainPageLocators, LoginPageLocators
from url import BASE_URL


class TestConstructorNavigation:

    def test_go_to_constructor_from_login_page_by_constructor_button(self, driver):
        driver.get(BASE_URL)

        wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT).click()
        wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)

        wait_for_clickable(driver, MainPageLocators.CONSTRUCTOR_BUTTON).click()

        assert wait_for_visible(driver, MainPageLocators.BURGER_SECTION).is_displayed()


    def test_go_to_constructor_from_login_page_by_logo(self, driver):
        driver.get(BASE_URL)

        wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT).click()
        wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)

        wait_for_clickable(driver, MainPageLocators.LOGO).click()

        assert wait_for_visible(driver, MainPageLocators.BURGER_SECTION).is_displayed()