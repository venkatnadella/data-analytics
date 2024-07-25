#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from app import load_data, analyze_data

def test_load_data():
    df = load_data('data/sample_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_analyze_data():
    df = load_data('data/sample_data.csv')
    summary = analyze_data(df)
    assert 'count' in summary.columns
    assert 'mean' in summary.columns
    assert 'std' in summary.columns


# In[ ]:




