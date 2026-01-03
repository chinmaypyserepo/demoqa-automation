from api.client.bookstore_api import BookStoreApiClient
import pytest

@pytest.mark.api
def test_books_api_returns_data():
    client = BookStoreApiClient()
    response = client.get_all_books()

    assert response.status_code == 200
    assert "books" in response.json()
    assert len(response.json()["books"]) > 0
    #jkk
