from helpers.generators import generate_email
from helpers import wait_for_clickable
from selenium.webdriver.common.by import By
from url import BASE_URL

def test_success_registration(driver):
    driver.get(BASE_URL + "/register")


def test_invalid_password_registration(driver):
    driver.get(BASE_URL + "/register") 