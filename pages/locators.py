from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка "Войти в аккаунт" на главной странице

    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    # Кнопка перехода в личный кабинет

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Кнопка перехода в конструктор


class LoginPageLocators:
    """Локаторы страницы логина"""

    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    # Поле ввода email

    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Поле ввода пароля

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка входа


class ProfilePageLocators:
    """Локаторы профиля пользователя"""

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка выхода из аккаунта


class ConstructorLocators:
    """Локаторы конструктора"""

    BUNS_TAB = (By.XPATH, "//span[contains(text(),'Булки')]")
    # Вкладка "Булки"

    SAUCES_TAB = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # Вкладка "Соусы"

    FILLINGS_TAB = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Вкладка "Начинки"


class RegisterPageLocators:
    """Локаторы страницы регистрации"""

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле имени

    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    # Поле email

    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Поле пароля

    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Кнопка регистрации