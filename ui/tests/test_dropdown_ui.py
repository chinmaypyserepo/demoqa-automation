import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.settings import UI_BASE_URL

@pytest.mark.ui
def test_dropdown_after_login(login_browser):
    login_browser.get(f"{UI_BASE_URL}/select-menu")
    dropdown = Select(login_browser.find_element(By.ID, "oldSelectMenu"))
    dropdown.select_by_visible_text("Blue")
    assert dropdown.first_selected_option.text == "Blue"
