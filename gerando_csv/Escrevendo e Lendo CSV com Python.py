# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:15:20 2018

@author: Gerson
"""

import pandas as pd

raw_data = {'X1': [2,1],
            'X2': [3,9]
        }
data = pd.DataFrame(raw_data, columns = ['X1','X2'])
data.to_csv('set.csv')

get_seet_data = pd.read_csv('set.csv')