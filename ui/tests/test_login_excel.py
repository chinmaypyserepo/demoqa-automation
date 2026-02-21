import pytest
from ui.pages.login_page import LoginPage
from utils.excel_reader import read_excel

@pytest.mark.ui
@pytest.mark.parametrize("username,password", read_excel("testdata/login_data.xlsx"))
def test_login_excel(browser, username, password):
    browser.get("https://the-internet.herokuapp.com/login")
    LoginPage(browser).login(username, password)