import unittest

import requests


class PunkAPITest(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://api.punkapi.com/v2/beers"

    def test_get_default_beers(self):
        res_body = requests.get(self.url).json()

        self.assertEqual(25, len(res_body))
        self.assertEqual(1, res_body[0]["id"])
        self.assertEqual(25, res_body[-1]["id"])

    def test_beer_123(self):
        res_body = requests.get(f"{self.url}/123").json()

        self.assertEqual(123, res_body[0]["id"])
        self.assertEqual(1, len(res_body))

    def test_80_from_2nd_page(self):
        params = {
            "page": 2,
            "per_page": 80
        }
        res_body = requests.get(self.url, params=params).json()
        self.assertEqual(80, len(res_body))
        self.assertEqual(81, res_body[0]["id"])
        self.assertEqual(160, res_body[-1]["id"])

    def test_beers_1_to_5(self):
        params = {
            "ids": "1|2|3|4|5"
        }
        res_body = requests.get(self.url, params=params).json()
        self.assertEqual(5, len(res_body))
        self.assertEqual(1, res_body[0]["id"])
        self.assertEqual(5, res_body[-1]["id"])

    def test_abv_5_to_7(self):
        params = {
            "abv_gt": 4.9,
            "abv_lt": 7.1
        }
        res_body = requests.get(self.url, params=params).json()
        for beer in res_body:
            self.assertGreaterEqual(beer["abv"], 5)
            self.assertLessEqual(beer["abv"], 7)

    def test_brewed_in_2010(self):

        params = {
            "brewed_before": "01-2011",
            "brewed_after": "12-2009"
        }
        res_body = requests.get(self.url, params=params).json()
        for beer in res_body:
            self.assertIn("2010", beer["first_brewed"])


if __name__ == '__main__':
    unittest.main()
