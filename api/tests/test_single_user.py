import pytest
from api.client.user_api import UserAPI

@pytest.mark.api
def test_single_user():
    api = UserAPI()
    response = api.get_single_user(2)
    assert response.status_code == 200