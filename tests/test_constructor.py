import pytest

from helpers.waits import wait_for_visible, safe_click, wait_overlay_disappear
from pages.locators import ConstructorLocators
from url import BASE_URL


class TestConstructor:

    @pytest.mark.parametrize(
        "tab, section",
        [
            (ConstructorLocators.BUNS_TAB, ConstructorLocators.BUNS_SECTION),
            (ConstructorLocators.SAUCES_TAB, ConstructorLocators.SAUCES_SECTION),
            (ConstructorLocators.FILLINGS_TAB, ConstructorLocators.FILLINGS_SECTION),
        ],
    )
    def test_constructor_tabs(self, driver, tab, section):
        try:
            driver.get(BASE_URL)

            wait_overlay_disappear(driver)

            element = wait_for_visible(driver, tab)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            safe_click(driver, tab)

            section_element = wait_for_visible(driver, section)

            assert section_element.is_displayed()

        finally:
            driver.quit()