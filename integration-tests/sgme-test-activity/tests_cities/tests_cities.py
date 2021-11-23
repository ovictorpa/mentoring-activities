import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class Cities(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_cities_id(self):
        auth = get_token()

        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/cities/{2}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('id', json_data)
        self.assertEqual(type(json_data['id']), int)

        self.assertIn('name', json_data)
        self.assertEqual(type(json_data['name']), str)

        self.assertIn('active', json_data)
        self.assertEqual(type(json_data['active']), bool)

        self.assertIn('state', json_data)
        self.assertEqual(type(json_data['state']), dict)

        self.assertIn('id', json_data['state'])
        self.assertEqual(type(json_data['state']['id']), int)

        self.assertIn('name', json_data['state'])
        self.assertEqual(type(json_data['state']['name']), str)

        self.assertIn('active', json_data['state'])
        self.assertEqual(type(json_data['state']['active']), bool)

        self.assertIn('country', json_data['state'])
        self.assertEqual(type(json_data['state']['country']), dict)

        self.assertIn('id', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['id']), int)

        self.assertIn('name', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['name']), str)

        self.assertIn('ddi', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['ddi']), int)

        self.assertIn('timezone', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['timezone']), dict)

        self.assertIn('id', json_data['state']['country']['timezone'])
        self.assertEqual(type(json_data['state']['country']['timezone']['id']), int)

        self.assertIn('name', json_data['state']['country']['timezone'])
        self.assertEqual(type(json_data['state']['country']['timezone']['name']), str)

        self.assertIn('timeAdjustment', json_data['state']['country']['timezone'])
        self.assertEqual(type(json_data['state']['country']['timezone']['timeAdjustment']), str)

        self.assertIn('active', json_data['state']['country']['timezone'])
        self.assertEqual(type(json_data['state']['country']['timezone']['active']), bool)

        self.assertIn('currencyName', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['currencyName']), str)

        self.assertIn('currencySymbol', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['currencySymbol']), str)

        self.assertIn('separator', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['separator']), str)

        self.assertIn('active', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['active']), bool)

        self.assertIn('adviserChangePermission', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['adviserChangePermission']), bool)

        self.assertIn('coordinatorChangePermission', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['coordinatorChangePermission']), bool)

        self.assertIn('forumByEditionPermission', json_data['state']['country'])
        self.assertEqual(type(json_data['state']['country']['forumByEditionPermission']), bool)

        self.assertIn('timezone', json_data['state'])
        self.assertEqual(type(json_data['state']['timezone']), dict)

        self.assertIn('id', json_data['state']['timezone'])
        self.assertEqual(type(json_data['state']['timezone']['id']), int)

        self.assertIn('name', json_data['state']['timezone'])
        self.assertEqual(type(json_data['state']['timezone']['name']), str)

        self.assertIn('timeAdjustment', json_data['state']['timezone'])
        self.assertEqual(type(json_data['state']['timezone']['timeAdjustment']), str)

        self.assertIn('active', json_data['state']['timezone'])
        self.assertEqual(type(json_data['state']['timezone']['active']), bool)