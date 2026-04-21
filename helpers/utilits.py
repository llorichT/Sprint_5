from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def safe_click(driver, element):
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)