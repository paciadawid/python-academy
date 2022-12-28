import unittest

from faker import Faker

from api_tests.src.gorest_api_handler import APIHandler


class TestIP(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler("56c3f5739c2af4edb091c270360c0d22f7f804005a9b598801b24ee6b3e45f8f")
        self.fake = Faker()

    def test_create_user(self):
        new_user = {
            "name": self.fake.name(),
            "gender": "male",
            "email": self.fake.email(),
            "status": "active"
        }
        response_body = self.api_handler.create_user(new_user)
        self.assertTrue(response_body["id"])
        user = self.api_handler.get_user(response_body["id"])
        self.assertDictContainsSubset(new_user, user)


if __name__ == '__main__':
    unittest.main()
