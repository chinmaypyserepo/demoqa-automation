import pytest
from api.client.user_api import UserAPI

@pytest.mark.api
def test_get_users():
    api = UserAPI()
    response = api.get_users()
    assert response.status_code == 200