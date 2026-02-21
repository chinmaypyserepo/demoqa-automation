import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class UserAPI:

    def get_users(self):
        return requests.get(f"{BASE_URL}/users")

    def get_single_user(self, user_id):
        return requests.get(f"{BASE_URL}/users/{user_id}")

    def create_user(self, name, job):
        payload = {
            "name": name,
            "username": name.lower(),
            "email": f"{name.lower()}@test.com"
        }
        return requests.post(f"{BASE_URL}/users", json=payload)