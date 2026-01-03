import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ---------------- BROWSER FIXTURE ----------------
@pytest.fixture
def browser(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    # attach driver to test node (needed for screenshot hook)
    request.node.driver = driver

    yield driver

    driver.quit()
# -------------------------------------------------


# -------- SCREENSHOT ON FAILURE (ALLURE) ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            screenshots_dir = "reports/failed/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_path)

            allure.attach.file(
                file_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
# -------------
