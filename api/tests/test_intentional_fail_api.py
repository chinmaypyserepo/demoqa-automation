import pytest

@pytest.mark.api
def test_intentional_fail_api():
    assert 1 == 5