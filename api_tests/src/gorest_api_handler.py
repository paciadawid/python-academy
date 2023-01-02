import requests


class APIHandler:
    url = "https://gorest.co.in/public/v2"
    users_endpoint = "/users"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def create_user(self, user_data, expected_status_code=201):
        res = requests.post(f"{self.url}{self.users_endpoint}", json=user_data, headers=self.headers)
        if expected_status_code:
            assert expected_status_code == res.status_code
        return res.json()

    def get_user(self, user_id, expected_status_code=200):
        res = requests.get(f"{self.url}{self.users_endpoint}/{user_id}", headers=self.headers)
        if expected_status_code:
            assert expected_status_code == res.status_code
        return res.json()

    def update_user(self, user_id, user_data, expected_status_code=200):
        res = requests.put(f"{self.url}{self.users_endpoint}/{user_id}", json=user_data, headers=self.headers)
        if expected_status_code:
            assert expected_status_code == res.status_code
        return res.json()

    def delete_user(self, user_id, expected_status_code=204):
        res = requests.delete(f"{self.url}{self.users_endpoint}/{user_id}", headers=self.headers)
        if expected_status_code:
            assert expected_status_code == res.status_code
