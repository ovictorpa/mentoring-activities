import unittest
import os
import sys
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features/steps/json_scenarios")
sys.path.append(path_dir)

from json_utils import *


class FinancialStrategy(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_financial_strategy_id(self):
        auth = get_token()
        header = {'Authorization': auth}
        response = requests.get(f'{self.url}/financial-strategy/{1572}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('salePrice', json_data)
        self.assertEqual(type(json_data['salePrice']), dict)

        salePrice = json_data['salePrice']

        self.assertIn('id', salePrice)
        self.assertEqual(type(salePrice['id']), int)

        self.assertIn('company', salePrice)
        self.assertEqual(type(salePrice['company']), dict)

        company = salePrice['company']

        self.assertIn('id', company)
        self.assertEqual(type(company['id']), int)

        self.assertIn('fixedCost', json_data)
        self.assertEqual(type(json_data['fixedCost']), dict)

        fixedCost = json_data['fixedCost']

        self.assertIn('office_supplies', fixedCost)
        self.assertEqual(type(fixedCost['office_supplies']), float)

        self.assertIn('formulas', json_data)
        self.assertEqual(type(json_data['formulas']), dict)

        formulas = json_data['formulas']

        self.assertIn('sumOfRentFixedCosts', formulas)
        self.assertEqual(type(formulas['sumOfRentFixedCosts']), float)

        self.assertIn('sumSalaryFixedCosts', formulas)
        self.assertEqual(type(formulas['sumSalaryFixedCosts']), float)

        self.assertIn('sumOfSocialChargesFixedCosts', formulas)
        self.assertEqual(type(formulas['sumOfSocialChargesFixedCosts']), float)

        self.assertIn('otherFixedCosts', formulas)
        self.assertEqual(type(formulas['otherFixedCosts']), float)

        self.assertIn('sumCommission', formulas)
        self.assertEqual(type(formulas['sumCommission']), float)

        self.assertIn('sumCommissionCharges', formulas)
        self.assertEqual(type(formulas['sumCommissionCharges']), float)

        self.assertIn('sumTaxForSale', formulas)
        self.assertEqual(type(formulas['sumTaxForSale']), float)

        self.assertIn('otherVariableCosts', formulas)
        self.assertEqual(type(formulas['otherVariableCosts']), float)

        self.assertIn('contribution', formulas)
        self.assertEqual(type(formulas['contribution']), float)

        self.assertIn('balance', formulas)
        self.assertEqual(type(formulas['balance']), float)

        self.assertIn('balanceNetProfit', formulas)
        self.assertEqual(type(formulas['balanceNetProfit']), float)

        self.assertIn('profit', formulas)
        self.assertEqual(type(formulas['profit']), float)

        self.assertIn('unitsToProduce', formulas)
        self.assertEqual(type(formulas['unitsToProduce']), float)

        self.assertIn('verifySalesGoalAndBreakevenPoint', json_data)
        self.assertEqual(type(json_data['verifySalesGoalAndBreakevenPoint']), bool)

        self.assertIn('hasActionsPermission', json_data)
        self.assertEqual(type(json_data['hasActionsPermission']), bool)

