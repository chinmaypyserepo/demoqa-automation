import pytest
from ui.pages.login_page import LoginPage

@pytest.mark.ui
def test_valid_login(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    LoginPage(browser).login("tomsmith", "SuperSecretPassword!")
    assert "secure" in browser.current_url