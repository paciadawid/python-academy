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

    def test_user_e2e_flo(self):
        new_user = {
            "name": self.fake.name(),
            "gender": "male",
            "email": self.fake.email(),
            "status": "active"
        }
        user_id = self.api_handler.create_user(new_user)["id"]
        self.assertTrue(user_id)

        update_data = {
            "name": self.fake.name()
        }
        user_data = self.api_handler.update_user(user_id, update_data)
        self.assertEqual(user_data["name"], update_data["name"])
        self.api_handler.delete_user(user_id)
        self.api_handler.get_user(user_id, expected_status_code=404)


if __name__ == '__main__':
    unittest.main()
