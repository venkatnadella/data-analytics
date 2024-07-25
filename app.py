#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def analyze_data(df):
    """Perform basic analysis on the DataFrame."""
    summary = df.describe()
    return summary

def plot_data(df):
    """Plot the data."""
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['value'], marker='o', linestyle='-')
    plt.title('Sample Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig('plot.png')
    plt.show()

def main():
    # Example usage
    df = load_data('data/sample_data.csv')
    summary = analyze_data(df)
    print(summary)
    plot_data(df)

if __name__ == "__main__":
    main()

