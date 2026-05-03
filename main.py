from eda.summary import enhanced_summary
from eda.missing import missing_values,missing_analysis
from eda.outliers import outlier_percentage
from eda.insights import generate_insights
from eda.correlation import correlation_analysis
from eda.plots import generate_histograms, correlation_heatmap
import pandas as pd
import json
import os

def run_eda(file_path):
    df = pd.read_csv(file_path)
    results = {}
    results['summary'] = enhanced_summary(df)
    results['missing'] = missing_values(df)
    results['missing_insights'] = missing_analysis(df)
    results['outliers'] = outlier_percentage(df)
    results['insights'] = generate_insights(df)
    results['correlation'] = correlation_analysis(df)
    results['histograms'] = generate_histograms(df)
    results['heatmap'] = correlation_heatmap(df)
    results["overview"] = f"""
Dataset has {df.shape[0]} rows and {df.shape[1]} columns.
Contains {len(df.select_dtypes(include='number').columns)} numeric features
and {len(df.select_dtypes(exclude='number').columns)} categorical features.
"""
    return results

if __name__ == '__main__':
    os.makedirs('static/outputs', exist_ok=True)
    results = run_eda('data/Titanic-Dataset.csv')
    with open('static/outputs/report.json', 'w') as f:
        json.dump(results, f, indent=4, default=str)
