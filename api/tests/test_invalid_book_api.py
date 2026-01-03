import pytest
from api.client.bookstore_api import BookStoreApiClient

@pytest.mark.api
def test_invalid_book():
    res = BookStoreApiClient().get_single_book("invalid")
    assert res.status_code == 400
