from pages.locators import LoginPageLocators
from data import EMAIL, PASSWORD


def login(driver):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()