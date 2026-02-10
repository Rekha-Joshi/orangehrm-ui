from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_page_load(driver):
    login = LoginPage(driver)
    assert login.is_loaded()

def test_valid_login(driver):
    # create instance of login page and send user name and password
    login = LoginPage(driver)
    assert login.is_loaded()
    login.login("Admin", "admin123")
    # create instance of dashboard page to check if login is successful or not
    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded()

