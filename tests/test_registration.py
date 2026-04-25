import pytest

from helpers.generators import generate_user_data, generate_password
from helpers.waits import wait_for_visible, safe_click
from pages.locators import RegisterPageLocators, LoginPageLocators
from url import REGISTER_URL, LOGIN_URL


def fill_registration_form(driver, name, email, password):
    wait_for_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(name)
    wait_for_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    wait_for_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(password)


class TestRegistration:

    def test_successful_registration(self, driver):
        user = generate_user_data()

        driver.get(REGISTER_URL)

        fill_registration_form(driver, user["name"], user["email"], user["password"])
        safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

        wait_for_visible(driver, LoginPageLocators.LOGIN_BUTTON)

        assert driver.current_url == LOGIN_URL


    def test_registration_invalid_password(self, driver):
        user = generate_user_data()

        driver.get(REGISTER_URL)

        fill_registration_form(driver, user["name"], user["email"], "123")
        safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

        error = wait_for_visible(driver, RegisterPageLocators.ERROR_MESSAGE)

        assert error.text == "Некорректный пароль"


    @pytest.mark.parametrize("invalid_email", [
        "test",
        "test@",
        "@mail.ru",
        "testmail.ru",
        "test@.ru",
    ])
    def test_registration_invalid_email(self, driver, invalid_email):
        user = generate_user_data()

        driver.get(REGISTER_URL)

        fill_registration_form(driver, user["name"], invalid_email, user["password"])
        safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

        error = wait_for_visible(driver, RegisterPageLocators.ERROR_MESSAGE)

        assert error.is_displayed()
        assert error.text != ""


    def test_registration_empty_name(self, driver):
        user = generate_user_data()

        driver.get(REGISTER_URL)

        fill_registration_form(driver, "", user["email"], user["password"])
        safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

        name_input = wait_for_visible(driver, RegisterPageLocators.NAME_INPUT)

        assert driver.current_url == REGISTER_URL
        assert name_input.is_displayed()