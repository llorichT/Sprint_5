from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""

    LOGIN_BUTTON = (By.XPATH, "//button[.//text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CSS_SELECTOR, "a[href='/']")
    BURGER_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")


class LoginPageLocators:
    """Локаторы страницы логина"""

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""

    LOGIN_LINK = (By.CSS_SELECTOR, "a[href*='login']")


class ProfilePageLocators:
    """Локаторы личного кабинета"""

    LOGOUT_BUTTON = (By.XPATH, "//button[.//text()='Выход']")


class ConstructorLocators:
    """Локаторы конструктора"""

    BUNS_TAB = (By.XPATH, "//div[contains(@class,'tab')]//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class,'tab')]//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class,'tab')]//span[text()='Начинки']")

    BUNS_SECTION = (By.XPATH, "//section//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//section//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//section//h2[text()='Начинки']")


class RegisterPageLocators:
    """Локаторы страницы регистрации"""

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")