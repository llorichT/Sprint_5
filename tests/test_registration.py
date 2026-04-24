import pytest

from helpers.generators import (
    generate_name,
    generate_surname,
    generate_cohort,
    generate_domain,
    generate_email,
    generate_password,
)
from helpers.waits import wait_for_visible, safe_click
from pages.locators import RegisterPageLocators, LoginPageLocators
from url import REGISTER_URL


def fill_registration_form(driver, name, email, password):
    wait_for_visible(driver, RegisterPageLocators.NAME_INPUT).send_keys(name)
    wait_for_visible(driver, RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    wait_for_visible(driver, RegisterPageLocators.PASSWORD_INPUT).send_keys(password)


def generate_valid_email():
    name = generate_name()
    surname = generate_surname()
    cohort = generate_cohort()
    domain = generate_domain()

    return generate_email(name, surname, cohort, domain)


class TestRegistration:

    def test_successful_registration(self, driver):
        try:
            name = generate_name()
            email = generate_valid_email()
            password = generate_password()

            driver.get(REGISTER_URL)

            fill_registration_form(driver, name, email, password)
            safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

            login_input = wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)

            assert login_input.is_displayed()

        finally:
            driver.quit()

    def test_registration_invalid_password(self, driver):
        try:
            name = generate_name()
            email = generate_valid_email()
            password = "123"

            driver.get(REGISTER_URL)

            fill_registration_form(driver, name, email, password)
            safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

            error = wait_for_visible(driver, RegisterPageLocators.ERROR_MESSAGE)

            assert error.is_displayed()
            assert error.text != ""

        finally:
            driver.quit()

    @pytest.mark.parametrize("invalid_email", [
        "test",
        "test@",
        "@mail.ru",
        "testmail.ru",
        "test@.ru",
    ])
    def test_registration_invalid_email(self, driver, invalid_email):
        try:
            name = generate_name()
            password = generate_password()

            driver.get(REGISTER_URL)

            fill_registration_form(driver, name, invalid_email, password)
            safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

            error = wait_for_visible(driver, RegisterPageLocators.ERROR_MESSAGE)

            assert error.is_displayed()
            assert error.text != ""

        finally:
            driver.quit()