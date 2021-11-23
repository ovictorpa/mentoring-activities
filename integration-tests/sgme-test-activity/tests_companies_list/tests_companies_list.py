import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class CompaniesList(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_post_companies_list(self):
        auth = get_token()
        header = {'Authorization': auth}
        params = {"start": 0, "max": 10}
        body = {"name":"teste"}
        response = requests.post(f'{self.url}/companies-list', headers=header, json=body, params=params)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for item in json_data['companies']:
            self.assertIn('id', item)
            self.assertEqual(type(item['id']), int)

            self.assertIn('name', item)
            self.assertEqual(type(item['name']), str)

            self.assertIn('key', item)
            self.assertEqual(type(item['key']), str)

            self.assertIn('edition', item)
            self.assertEqual(type(item['edition']), dict)

            self.assertIn('name', item['edition'])
            self.assertEqual(type(item['edition']['name']), str)

            self.assertIn('startDate', item['edition'])
            self.assertEqual(type(item['edition']['startDate']), str)

            self.assertIn('institution', item)
            self.assertEqual(type(item['institution']), dict)

            self.assertIn('name', item['institution'])
            self.assertEqual(type(item['institution']['name']), str)

            self.assertIn('city', item['institution'])
            self.assertEqual(type(item['institution']['city']), dict)

            self.assertIn('name', item['institution']['city'])
            self.assertEqual(type(item['institution']['city']['name']), str)

            self.assertIn('state', item['institution']['city'])
            self.assertEqual(type(item['institution']['city']['state']), dict)

            self.assertIn('name', item['institution']['city']['state'])
            self.assertEqual(type(item['institution']['city']['state']['name']), str)

            self.assertIn('country', item['institution']['city']['state'])
            self.assertEqual(type(item['institution']['city']['state']['country']), dict)

            self.assertIn('name', item['institution']['city']['state']['country'])
            self.assertEqual(type(item['institution']['city']['state']['country']['name']), str)

        self.assertIn('totalList', json_data)
        self.assertEqual(type(json_data['totalList']), int)

        print()