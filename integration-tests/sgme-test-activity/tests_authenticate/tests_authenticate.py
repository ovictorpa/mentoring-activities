import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class Authenticate(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_post_authenticate_login(self):
        body = get_valid_credentials()
        response = requests.post(f'{self.url}/authenticate/login', json=body)
        assert response.status_code == 200
        json_data = json.loads(response.text)

        self.assertIn('id', json_data)
        self.assertEqual(type(json_data['id']), int)

        self.assertIn('name', json_data)
        self.assertEqual(type(json_data['name']), str)

        self.assertIn('email', json_data)
        self.assertEqual(type(json_data['email']), str)

        self.assertIn('phone', json_data)
        self.assertEqual(type(json_data['phone']), str)

        self.assertIn('profile', json_data)
        self.assertEqual(type(json_data['profile']), dict)

        self.assertIn('avatar', json_data)
        self.assertEqual(type(json_data['avatar']), str)

        self.assertIn('lastAccess', json_data)
        self.assertEqual(type(json_data['lastAccess']), str)

        self.assertIn('state', json_data)
        self.assertEqual(type(json_data['state']), dict)

        self.assertIn('country', json_data)
        self.assertEqual(type(json_data['country']), dict)

        self.assertIn('language', json_data)
        self.assertEqual(type(json_data['language']), dict)

        self.assertIn('accessibility', json_data)
        self.assertEqual(type(json_data['accessibility']), str)

        self.assertIn('active', json_data)
        self.assertEqual(type(json_data['active']), bool)

        for permission in json_data['permissions']:
            self.assertIn('tag', permission)
            self.assertEqual(type(permission['tag']), str)

            self.assertIn('name', permission)
            self.assertEqual(type(permission['name']), str)

        self.assertIn('token', json_data)
        self.assertEqual(type(json_data['token']), str)

        self.assertIn('logged', json_data)
        self.assertEqual(type(json_data['logged']), bool)




        print()
