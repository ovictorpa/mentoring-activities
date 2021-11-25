import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class Dashboard(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_dashboard_id(self):
        auth = get_token()
        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/dashboard/{1572}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for journeys in json_data['journeys']:
            self.assertIn('id', journeys)
            self.assertEqual(type(journeys['id']), int)

            self.assertIn('sort_order', journeys)
            self.assertEqual(type(journeys['sort_order']), int)

            self.assertIn('current', journeys)
            self.assertEqual(type(journeys['current']), bool)

            self.assertIn('open', journeys)
            self.assertEqual(type(journeys['open']), bool)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']), dict)

        self.assertIn('breakevenPoint', json_data['goals'])
        self.assertEqual(type(json_data['goals']['breakevenPoint']), float)

        self.assertIn('salesGoal', json_data['goals'])
        self.assertEqual(type(json_data['goals']['salesGoal']), float)

        self.assertIn('totalTaxForSale', json_data['goals'])
        self.assertEqual(type(json_data['goals']['totalTaxForSale']), float)

        self.assertIn('unitBP', json_data['goals'])
        self.assertEqual(type(json_data['goals']['unitBP']), float)

        self.assertIn('unitSG', json_data['goals'])
        self.assertEqual(type(json_data['goals']['unitSG']), float)

        self.assertIn('progress', json_data)
        self.assertEqual(type(json_data['progress']), dict)

        self.assertIn('progressPlaning', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressPlaning']), float)

        self.assertIn('progressRH', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressRH']), float)

        self.assertIn('progressProduction', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressProduction']), int)

        self.assertIn('progressMarketing', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressMarketing']), int)

        self.assertIn('progressFinancial', json_data['progress'])
        self.assertEqual(type(json_data['progress']['progressFinancial']), float)

        self.assertIn('saleDevolutionInfo', json_data)
        self.assertEqual(type(json_data['saleDevolutionInfo']), dict)

        self.assertIn('retired', json_data['saleDevolutionInfo'])
        self.assertEqual(type(json_data['saleDevolutionInfo']['retired']), int)

        self.assertIn('stock', json_data['saleDevolutionInfo'])
        self.assertEqual(type(json_data['saleDevolutionInfo']['stock']), int)

        self.assertIn('totalProductsSelled', json_data)
        self.assertEqual(type(json_data['totalProductsSelled']), float)

        self.assertIn('percentAveragePresence', json_data)
        self.assertEqual(type(json_data['percentAveragePresence']), float)

        self.assertIn('formulas', json_data)
        self.assertEqual(type(json_data['formulas']), dict)

        self.assertIn('actionsProfitability', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['actionsProfitability']), float)

        self.assertIn('totalShareCapital', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['totalShareCapital']), float)

        self.assertIn('productionGoal', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['productionGoal']), float)

        self.assertIn('saleGoal', json_data['formulas'])
        self.assertEqual(type(json_data['formulas']['saleGoal']), float)

        self.assertIn('dre1', json_data)
        self.assertEqual(type(json_data['dre1']), dict)

        self.assertIn('provider', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['provider']), float)

        self.assertIn('income', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['income']), float)

        self.assertIn('sales', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['sales']), float)

        self.assertIn('rent', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['rent']), float)

        self.assertIn('taxForSales', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['taxForSales']), float)

        self.assertIn('socialCompanyCharges', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['socialEmployeeCharges']), float)

        self.assertIn('comissions', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['comissions']), float)

        self.assertIn('netProfit', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['netProfit']), float)

        self.assertIn('taxes', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['taxes']), float)

        self.assertIn('finalProfit', json_data['dre1'])
        self.assertEqual(type(json_data['dre1']['finalProfit']), float)

        self.assertIn('dre2', json_data)
        self.assertEqual(type(json_data['dre2']), dict)

        self.assertIn('provider', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['provider']), float)

        self.assertIn('income', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['income']), float)

        self.assertIn('sales', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['sales']), float)

        self.assertIn('rent', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['rent']), float)

        self.assertIn('taxForSales', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['taxForSales']), float)

        self.assertIn('socialCompanyCharges', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['socialEmployeeCharges']), float)

        self.assertIn('comissions', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['comissions']), float)

        self.assertIn('netProfit', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['netProfit']), float)

        self.assertIn('taxes', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['taxes']), float)

        self.assertIn('finalProfit', json_data['dre2'])
        self.assertEqual(type(json_data['dre2']['finalProfit']), float)

        print()