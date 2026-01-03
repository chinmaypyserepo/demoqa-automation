import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.login_page import LoginPage
from config.settings import UI_BASE_URL


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.node.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def login_browser(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get(f"{UI_BASE_URL}/login")
    LoginPage(driver).login("dummy", "dummy")

    request.node.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            os.makedirs("reports/failed/screenshots", exist_ok=True)
            path = f"reports/failed/screenshots/{item.name}.png"
            driver.save_screenshot(path)
            allure.attach.file(path, name="Failure Screenshot",
                               attachment_type=allure.attachment_type.PNG)
