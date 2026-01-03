import requests

class BookStoreApiClient:
    BASE_URL = "https://demoqa.com/BookStore/v1"

    def get_all_books(self):
        return requests.get(f"{self.BASE_URL}/Books")

    def get_single_book(self, isbn):
        return requests.get(
            f"{self.BASE_URL}/Book",
            params={"ISBN": isbn}
        )
