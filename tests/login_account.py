from data import EMAIL, PASSWORD, BASE_URL
from helpers.waits import wait_for_clickable
from pages.locators import LoginPageLocators

def test_login_from_personal_account(driver):
    driver.get(BASE_URL)

    wait_for_clickable(driver, MainPageLocators.PERSONAL_ACCOUNT).click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)

    wait_for_clickable(driver, LoginPageLocators.LOGIN_BUTTON).click()

    assert "/account/profile" in driver.current_url