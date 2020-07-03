# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:53:37 2020

@author: mattw
"""


import unittest
from app import SiteUtils
import pandas as pd

class AppTest(unittest.TestCase):
    def test_request_active_covid_cases(self):
        utils = SiteUtils()
        cases = utils.requests_active_covid_cases()
        self.assertEqual(cases.status_code, 200)


    def test_prepare_data(self):
        utils = SiteUtils()
        df = utils.prepare_data
        self.assertIsInstance(df, pd.core.frame.DataFrame)