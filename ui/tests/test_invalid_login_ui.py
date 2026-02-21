import pytest
from ui.pages.login_page import LoginPage

@pytest.mark.ui
def test_invalid_login(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    LoginPage(browser).login("wrong", "wrong")
    assert "login" in browser.current_url