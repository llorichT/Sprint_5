from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""

    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    LOGO = (By.CSS_SELECTOR, "a[href='/']")  # Логотип Stellar Burgers
    BURGER_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок конструктора


class LoginPageLocators:
    """Локаторы страницы логина"""

    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка "Восстановить пароль"


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""

    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"


class ProfilePageLocators:
    """Локаторы личного кабинета"""

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"


class ConstructorLocators:
    """Локаторы конструктора"""

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"

    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Раздел "Начинки"


class RegisterPageLocators:
    """Локаторы страницы регистрации"""

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле имя
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле пароль
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  # Кнопка регистрации
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")  # Ссылка "Войти"
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")  # Ошибка регистрации