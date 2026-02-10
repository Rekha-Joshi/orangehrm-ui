from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(.,'Invalid credentials')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        return True
    
    def login(self, username: str , password: str):
        #username
        user_el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        user_el.clear()
        user_el.send_keys(username)

        #passeord
        pass_el = self.driver.find_element(*self.PASSWORD_INPUT)
        pass_el.clear()
        pass_el.send_keys(password)

        #click login button
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait.until(EC.url_contains("/dashboard"))