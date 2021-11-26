import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *

class UsersList(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_post_users_list(self):
        auth = get_token()
        header = {'Authorization': auth}
        params = {"start": 0, "max": 10}
        body = {
            "name": "Victor",
            "email": "victor.alves@dellead.com",
            "lastAccess": "",
            "profile": "",
            "country": "",
            "state": "",
            "institution": "",
            "responsible": "",
            "active": "true"
        }

        response = requests.post(f'{self.url}/users-list', headers=header, json=body, params=params)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for list in json_data['list']:
            self.assertIn('id', list)
            self.assertEqual(type(list['id']), int)

            self.assertIn('name', list)
            self.assertEqual(type(list['name']), str)

            self.assertIn('email', list)
            self.assertEqual(type(list['email']), str)

            self.assertIn('lastAccess', list)
            self.assertEqual(type(list['lastAccess']), str)

            self.assertIn('profile', list)
            self.assertEqual(type(list['profile']), dict)

            profile = list['profile']

            self.assertIn('id', profile)
            self.assertEqual(type(profile['id']), int)

            self.assertIn('name', profile)
            self.assertEqual(type(profile['name']), str)

            self.assertIn('country', list)
            self.assertEqual(type(list['country']), dict)

            country = list['country']

            self.assertIn('id', country)
            self.assertEqual(type(country['id']), int)

            self.assertIn('name', country)
            self.assertEqual(type(country['name']), str)

            self.assertIn('state', list)
            self.assertEqual(type(list['state']), dict)

            state = list['state']

            self.assertIn('id', state)
            self.assertEqual(type(state['id']), int)

            self.assertIn('name', state)
            self.assertEqual(type(state['name']), str)

            self.assertIn('institution', list)
            self.assertEqual(type(list['institution']), str)

            self.assertIn('active', list)
            self.assertEqual(type(list['active']), bool)

        self.assertIn('total', json_data)
        self.assertEqual(type(json_data['total']), int)


        print()