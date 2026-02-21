import pytest
from api.client.user_api import UserAPI
from utils.schema_validator import validate_schema
@pytest.mark.api
def test_schema_validation():
    api = UserAPI()
    response = api.get_users()

    assert response.status_code == 200

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["id", "name", "username", "email"]
        }
    }

    validate_schema(response.json(), schema)