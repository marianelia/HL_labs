import unittest
import requests


class TestAPI(unittest.TestCase):
    uri = "http://localhost:8080/api/users"

    def test_new_user(self):
        data = {
            "urser_login": "qqqq",
            "first_name": "AAAA",
            "second_name": "BBBBB",
            "password": "11111"
        }
        response = requests.post(f"{self.uri}/new_user", json=data)
        self.assertEqual(response.status_code, 200)

    def test_find_by_name(self):
        response = requests.get(
            f"{self.uri}/find_by_name?first_name=AAAA&second_name=BBBBB")
        self.assertEqual(response.status_code, 200)

    def test_find_by_login(self):
        response = requests.get(f"{self.uri}/find_by_login?login=admin")
        self.assertEqual(response.status_code, 200)

    def test_user_info(self):
        response = requests.get(f"{self.uri}/user_info?id=1")
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = requests.delete(f"{self.uri}/delete?user_id=10")
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        data = {
            "first_name": "AAAA"
        }
        response = requests.put(
            f"{self.uri}/update?user_id=11", json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
