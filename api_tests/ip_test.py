import unittest

import requests


class TestIP(unittest.TestCase):

    def test_my_ip(self):
        response_body = requests.get("https://api.ipify.org/?format=json").json()
        self.assertTrue(response_body["ip"])
        # self.assertRegex(response_body["ip"], "[0-9]{4}")


if __name__ == '__main__':
    unittest.main()
