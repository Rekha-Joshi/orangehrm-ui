from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout(driver):
    login = LoginPage(driver)
    assert login.is_loaded()
    login.login("Admin","admin123")

    dashboard = DashboardPage(driver)
    dashboard.is_loaded()
    dashboard.logout()
    assert "auth/login" in driver.current_url.lower()
    assert login.is_loaded()