import pandas as pd
from app import load_data, analyze_data

def test_load_data():
    df = load_data('data/sample_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_analyze_data():
    df = load_data('data/sample_data.csv')
    summary = analyze_data(df)
    assert 'index' in summary.columns
    assert 'value' in summary.columns





