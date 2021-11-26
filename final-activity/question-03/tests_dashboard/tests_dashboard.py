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

        goals = json_data['goals']

        self.assertIn('breakevenPoint', goals)
        self.assertEqual(type(goals['breakevenPoint']), float)

        self.assertIn('salesGoal', goals)
        self.assertEqual(type(goals['salesGoal']), float)

        self.assertIn('totalTaxForSale', goals)
        self.assertEqual(type(goals['totalTaxForSale']), float)

        self.assertIn('unitBP', goals)
        self.assertEqual(type(goals['unitBP']), float)

        self.assertIn('unitSG', goals)
        self.assertEqual(type(goals['unitSG']), float)

        self.assertIn('progress', json_data)
        self.assertEqual(type(json_data['progress']), dict)

        progress = json_data['progress']

        self.assertIn('progressPlaning', progress)
        self.assertEqual(type(progress['progressPlaning']), float)

        self.assertIn('progressRH', progress)
        self.assertEqual(type(progress['progressRH']), float)

        self.assertIn('progressProduction', progress)
        self.assertEqual(type(progress['progressProduction']), int)

        self.assertIn('progressMarketing', progress)
        self.assertEqual(type(progress['progressMarketing']), int)

        self.assertIn('progressFinancial', progress)
        self.assertEqual(type(progress['progressFinancial']), float)

        self.assertIn('saleDevolutionInfo', json_data)
        self.assertEqual(type(json_data['saleDevolutionInfo']), dict)

        saleDevolutionInfo = json_data['saleDevolutionInfo']

        self.assertIn('retired', saleDevolutionInfo)
        self.assertEqual(type(saleDevolutionInfo['retired']), int)

        self.assertIn('stock', saleDevolutionInfo)
        self.assertEqual(type(saleDevolutionInfo['stock']), int)

        self.assertIn('totalProductsSelled', json_data)
        self.assertEqual(type(json_data['totalProductsSelled']), float)

        self.assertIn('percentAveragePresence', json_data)
        self.assertEqual(type(json_data['percentAveragePresence']), float)

        self.assertIn('formulas', json_data)
        self.assertEqual(type(json_data['formulas']), dict)

        formulas = json_data['formulas']

        self.assertIn('actionsProfitability', formulas)
        self.assertEqual(type(formulas['actionsProfitability']), float)

        self.assertIn('totalShareCapital', formulas)
        self.assertEqual(type(formulas['totalShareCapital']), float)

        self.assertIn('productionGoal', formulas)
        self.assertEqual(type(formulas['productionGoal']), float)

        self.assertIn('saleGoal', formulas)
        self.assertEqual(type(formulas['saleGoal']), float)

        self.assertIn('dre1', json_data)
        self.assertEqual(type(json_data['dre1']), dict)

        dre1 = json_data['dre1']

        self.assertIn('provider', dre1)
        self.assertEqual(type(dre1['provider']), float)

        self.assertIn('income', dre1)
        self.assertEqual(type(dre1['income']), float)

        self.assertIn('sales', dre1)
        self.assertEqual(type(dre1['sales']), float)

        self.assertIn('rent', dre1)
        self.assertEqual(type(dre1['rent']), float)

        self.assertIn('taxForSales', dre1)
        self.assertEqual(type(dre1['taxForSales']), float)

        self.assertIn('socialCompanyCharges', dre1)
        self.assertEqual(type(dre1['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', dre1)
        self.assertEqual(type(dre1['socialEmployeeCharges']), float)

        self.assertIn('comissions', dre1)
        self.assertEqual(type(dre1['comissions']), float)

        self.assertIn('netProfit', dre1)
        self.assertEqual(type(dre1['netProfit']), float)

        self.assertIn('taxes', dre1)
        self.assertEqual(type(dre1['taxes']), float)

        self.assertIn('finalProfit', dre1)
        self.assertEqual(type(dre1['finalProfit']), float)

        self.assertIn('dre2', json_data)
        self.assertEqual(type(json_data['dre2']), dict)

        dre2 = json_data['dre2']

        self.assertIn('provider', dre2)
        self.assertEqual(type(dre2['provider']), float)

        self.assertIn('income', dre2)
        self.assertEqual(type(dre2['income']), float)

        self.assertIn('sales', dre2)
        self.assertEqual(type(dre2['sales']), float)

        self.assertIn('rent', dre2)
        self.assertEqual(type(dre2['rent']), float)

        self.assertIn('taxForSales', dre2)
        self.assertEqual(type(dre2['taxForSales']), float)

        self.assertIn('socialCompanyCharges', dre2)
        self.assertEqual(type(dre2['socialCompanyCharges']), float)

        self.assertIn('socialEmployeeCharges', dre2)
        self.assertEqual(type(dre2['socialEmployeeCharges']), float)

        self.assertIn('comissions', dre2)
        self.assertEqual(type(dre2['comissions']), float)

        self.assertIn('netProfit', dre2)
        self.assertEqual(type(dre2['netProfit']), float)

        self.assertIn('taxes', dre2)
        self.assertEqual(type(dre2['taxes']), float)

        self.assertIn('finalProfit', dre2)
        self.assertEqual(type(dre2['finalProfit']), float)

        print()