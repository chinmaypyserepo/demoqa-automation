import pytest
from api.client.user_api import UserAPI
from utils.excel_reader import read_excel

@pytest.mark.api
@pytest.mark.parametrize("name,job", read_excel("testdata/api_user_data.xlsx"))
def test_create_user_excel(name, job):
    api = UserAPI()
    response = api.create_user(name, job)
    assert response.status_code == 201