import unittest
from api_tests.src.helpers import *

from api_tests.src.pokeapi_api_handler import APIHandler


class TestPokemons(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_default_pokemons(self):
        response = self.api_handler.get_pokemons()
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

    def test_pokemon_shape_match_id_name(self):
        response_body = self.api_handler.get_shapes()
        self.assertEqual(response_body["count"], len(response_body["results"]))
        third_shape = response_body["results"][2]["name"]

        response_body = self.api_handler.get_shapes(name_or_id=third_shape)
        self.assertEqual(3, response_body["id"])

    def test_random_pokemon(self):
        random_id = get_random_id(1, 905)
        response_body = self.api_handler.get_pokemons(name_or_id=random_id)
        name = response_body["name"]
        response_body = self.api_handler.get_pokemons(name_or_id=name)
        self.assertTrue(response_body["abilities"])
        self.assertGreater(len(response_body["abilities"]), 0)


if __name__ == '__main__':
    unittest.main()
