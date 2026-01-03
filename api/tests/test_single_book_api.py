import pytest
from api.client.bookstore_api import BookStoreApiClient

@pytest.mark.api
def test_single_book():
    res = BookStoreApiClient().get_single_book("9781449325862")
    assert res.status_code == 200
