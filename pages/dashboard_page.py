from operator import truediv
from pickle import TRUE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage():
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.USER_DROPDOWN))
        return TRUE
    
    def logout(self):
        self.wait.until(EC.visibility_of_element_located(self.USER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
        #self.driver.find_element(*self.LOGOUT_LINK).click()
        self.wait.until(EC.url_contains("/login"))