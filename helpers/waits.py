from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DEFAULT_TIMEOUT = 10

OVERLAY_LOCATOR = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")


def wait_for_visible(driver, locator, timeout=DEFAULT_TIMEOUT):

    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):

    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_present(driver, locator, timeout=DEFAULT_TIMEOUT):

    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_overlay_disappear(driver, timeout=DEFAULT_TIMEOUT):

    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(OVERLAY_LOCATOR)
    )


def safe_click(driver, locator, timeout=DEFAULT_TIMEOUT):

    element = wait_for_clickable(driver, locator, timeout)

    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)

    return element