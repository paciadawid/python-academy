import unittest

import requests


class TestPokemons(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://pokeapi.co/api/v2"
        self.pokemon_endpoint = "/pokemon"

    def test_default_pokemons(self):
        response = requests.get(self.url + self.pokemon_endpoint)
        response_body = response.json()
        response_time = response.elapsed.microseconds // 1000
        self.assertTrue(response_body)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1154, response_body["count"])
        self.assertLess(response_time, 1000)
        self.assertLess(len(response.content), 100*1000)


if __name__ == '__main__':
    unittest.main()
