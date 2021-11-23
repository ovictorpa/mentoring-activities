import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class Profiles(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_profiles(self):
        auth = get_token()

        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/profiles', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for item in json_data:
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)

            self.assertIn('name', item)
            self.assertEqual(type(item['name']), str)

            self.assertIn('type', item)
            self.assertEqual(type(item['type']), str)