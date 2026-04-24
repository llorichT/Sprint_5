from pages.locators import LoginPageLocators, RegisterPageLocators
from helpers.generators import generate_user_data
from helpers.waits import wait_for_visible, safe_click
from url import REGISTER_URL

def enter_email(driver, email):
    email_input = wait_for_visible(driver, LoginPageLocators.EMAIL_INPUT)
    email_input.clear()
    email_input.send_keys(email)


def enter_password(driver, password):
    password_input = wait_for_visible(driver, LoginPageLocators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(password)


def click_login_button(driver):
    safe_click(driver, LoginPageLocators.LOGIN_BUTTON)


def login(driver, email, password):
    enter_email(driver, email)
    enter_password(driver, password)
    click_login_button(driver)


def enter_name(driver, name):
    name_input = wait_for_visible(driver, RegisterPageLocators.NAME_INPUT)
    name_input.clear()
    name_input.send_keys(name)


def enter_registration_email(driver, email):
    email_input = wait_for_visible(driver, RegisterPageLocators.EMAIL_INPUT)
    email_input.clear()
    email_input.send_keys(email)


def enter_registration_password(driver, password):
    password_input = wait_for_visible(driver, RegisterPageLocators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(password)


def click_register_button(driver):
    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)


def fill_registration_form(driver, name, email, password):
    enter_name(driver, name)
    enter_registration_email(driver, email)
    enter_registration_password(driver, password)


def register_user(driver, name, email, password):
    driver.get(REGISTER_URL)
    fill_registration_form(driver, name, email, password)
    click_register_button(driver)


def create_user():
    return generate_user_data()


def register_generated_user(driver):
    user = create_user()
    register_user(driver, user["name"], user["email"], user["password"])
    return user
