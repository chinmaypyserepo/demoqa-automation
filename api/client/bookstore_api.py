import requests
from config.settings import API_BASE_URL


class BookStoreApiClient:
    def get_all_books(self):
        return requests.get(f"{API_BASE_URL}/Books")
