import os

import requests


class APIHandler:
    url = "https://gorest.co.in/public"
    api_ver_dict = {
        "v1": "/v1",
        "v2": "/v2",
        "public": "/public-api"
    }
    users_endpoint = "/users"

    def __init__(self, token="", api_ver="v2"):
        self.url = f"{self.url}{api_ver}"
        if not token:
            token = os.environ["GOREST_TOKEN"]
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
