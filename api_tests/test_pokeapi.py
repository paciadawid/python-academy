import unittest

import requests

from api_tests.api_handler import APIHandler


class TestPokemons(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_default_pokemons(self):
        response = requests.get(self.url + self.pokemon_endpoint)
        response_body = response.json()
        response_time = response.elapsed.microseconds // 1000
        self.assertTrue(response_body)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1154, response_body["count"])
        self.assertLess(response_time, 1000)
        self.assertLess(len(response.content), 100 * 1000)

    def test_pokemons_with_limit_and_offset(self):
        params = {
            "limit": 10,
            "offset": 20
        }
        response_body = self.api_handler.get_pokemons(params=params)

        self.assertEqual(params["limit"], len(response_body["results"]))
        self.assertRegex(response_body["results"][0]["url"], f"/{params['offset'] + 1}")
        self.assertIn(f"/{params['offset'] + 1}", response_body["results"][0]["url"])


if __name__ == '__main__':
    unittest.main()
