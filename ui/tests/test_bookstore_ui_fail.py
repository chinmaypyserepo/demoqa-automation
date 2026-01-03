import pytest

@pytest.mark.ui
def test_intentional_failure(login_browser):
    assert False
