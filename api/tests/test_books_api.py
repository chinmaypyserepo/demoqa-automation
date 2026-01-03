import pytest
from api.client.bookstore_api import BookStoreApiClient

@pytest.mark.api
def test_get_books():
    res = BookStoreApiClient().get_all_books()
    assert res.status_code == 200
    assert len(res.json()["books"]) > 0
