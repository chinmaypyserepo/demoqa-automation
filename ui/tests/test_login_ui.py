import pytest
from config.settings import UI_BASE_URL

@pytest.mark.ui
def test_login_page_accessible(browser):
    browser.get(f"{UI_BASE_URL}/login")
    assert "login" in browser.current_url.lower()
