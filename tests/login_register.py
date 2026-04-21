from data import EMAIL, PASSWORD, BASE_URL
from helpers.waits import wait_for_clickable
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators


def test_login_from_register_page(driver):
    driver.get(f"{BASE_URL}/register")

    wait_for_clickable(driver, (By.XPATH, "//a[text()='Войти']")).click()

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)

    wait_for_clickable(driver, LoginPageLocators.LOGIN_BUTTON).click()

    assert "/account/profile" in driver.current_url