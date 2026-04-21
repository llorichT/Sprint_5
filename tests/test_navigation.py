from data import BASE_URL
from pages.locators import MainPageLocators
from helpers import wait_for_clickable, safe_click


def test_go_to_constructor(driver):
    driver.get(BASE_URL)

    personal_account = wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT)
    safe_click(driver, personal_account)

    constructor_button = wait_for_clickable(driver, MainPageLocators.CONSTRUCTOR_BUTTON)
    safe_click(driver, constructor_button)