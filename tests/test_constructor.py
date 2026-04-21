from data import BASE_URL
from pages.locators import ConstructorLocators
from helpers import wait_for_clickable, safe_click


def test_switch_to_buns(driver):
    driver.get(BASE_URL)

    buns_tab = wait_for_clickable(driver, ConstructorLocators.BUNS_TAB)
    safe_click(driver, buns_tab)


def test_switch_to_sauces(driver):
    driver.get(BASE_URL)

    sauces_tab = wait_for_clickable(driver, ConstructorLocators.SAUCES_TAB)
    safe_click(driver, sauces_tab)


def test_switch_to_fillings(driver):
    driver.get(BASE_URL)

    fillings_tab = wait_for_clickable(driver, ConstructorLocators.FILLINGS_TAB)
    safe_click(driver, fillings_tab)