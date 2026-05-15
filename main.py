from eda.summary import enhanced_summary
from eda.missing import missing_values,missing_analysis
from eda.outliers import outlier_percentage
from eda.insights import generate_insights
from eda.correlation import correlation_analysis
from eda.plots import generate_histograms, correlation_heatmap
from eda.quality import data_quality_score
import pandas as pd
import json
import os

def run_eda(file_path):
    df = pd.read_csv(file_path)

    results = {}

    # Overview
    results["overview"] = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_cols": len(df.select_dtypes(include='number').columns),
        "categorical_cols": len(df.select_dtypes(exclude='number').columns)
    }
    

    # Core analysis
    results["summary"] = enhanced_summary(df)
    results["missing"] = missing_values(df)
    results["outliers"] = outlier_percentage(df)
    results["correlation"] = correlation_analysis(df)

    # Data quality score
    score, score_issues = data_quality_score(
        df,
        results["missing"],
        results["outliers"],
        results["correlation"]
    )
    results["quality_score"] = score
    results["quality_issues"] = score_issues
    
    # Combine warnings
    results["warnings"] = []
    results["warnings"] += missing_analysis(df)
    results["warnings"] += generate_insights(df)

    # Visuals
    results["histograms"] = generate_histograms(df)
    results["heatmap"] = correlation_heatmap(df)

    


    return results

if __name__ == '__main__':
    os.makedirs('static/outputs', exist_ok=True)
    results = run_eda('data/Titanic-Dataset.csv')
    with open('static/outputs/report.json', 'w') as f:
        json.dump(results, f, indent=4, default=str)
