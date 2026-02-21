import pytest

@pytest.mark.ui
def test_intentional_fail_ui():
    assert "QA" == "Developer"