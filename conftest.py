import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    print("Launching browser:", browser_name)

    if browser_name == "firefox":
        driver = webdriver.Firefox(
            service=FFService(GeckoDriverManager().install())
        )

    elif browser_name == "edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )

    else:   # default chrome
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser", None)

        if driver:
            try:
                os.makedirs("reports/screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{item.name}_{timestamp}.png"
                driver.save_screenshot(f"reports/screenshots/{file_name}")
            except Exception:
                pass