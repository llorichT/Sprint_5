from data import EMAIL, PASSWORD, BASE_URL
from pages.locators import MainPageLocators, LoginPageLocators
from helpers import wait_for_clickable, safe_click


def test_login_from_main_button(driver):
    driver.get(BASE_URL)

    login_button_main = wait_for_clickable(driver, MainPageLocators.LOGIN_BUTTON)
    safe_click(driver, login_button_main)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)

    login_button = wait_for_clickable(driver, LoginPageLocators.LOGIN_BUTTON)
    safe_click(driver, login_button)