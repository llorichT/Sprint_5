from data import EMAIL, PASSWORD, BASE_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers.waits import wait_for_clickable


def test_logout(driver):
    driver.get(BASE_URL)

    wait_for_clickable(driver, MainPageLocators.LOGIN_BUTTON).click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)

    wait_for_clickable(driver, LoginPageLocators.LOGIN_BUTTON).click()

    wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT).click()

    wait_for_clickable(driver, ProfilePageLocators.LOGOUT_BUTTON).click()

    assert "/login" in driver.current_url