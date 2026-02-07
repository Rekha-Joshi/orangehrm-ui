from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()