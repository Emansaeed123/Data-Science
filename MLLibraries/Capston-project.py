#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eman-saeed
"""

#Data Capstone Project

"""
- Data set downloaded from kaggle
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('911.csv')
print(df.head())
print(df['zip'].value_counts().head())
x = df['title'].iloc[0]
x.split(":")[1]
df.info()
df['Hour'] = df['timeStamp'].apply(lambda time : time.hour)
df['Day of week '] = df['Day of week'].map(dmap)
df.head()
sns.countplot()
