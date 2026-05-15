import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(df):
    results = []

    for col in df.select_dtypes(include='number'):
        plt.figure()
        df[col].hist()
        path=f"static/outputs/{col}_hist.png"
        plt.savefig(path)
        plt.close()
        col_data = df[col].dropna()
        if len(col_data) > 0:
            mean = col_data.mean()
            median = col_data.median()
            minimum = col_data.min()
            maximum = col_data.max()
            
            skewness = col_data.skew()
            if skewness > 1:
                shape = "is highly right-skewed (most values are clustered on the lower end, with a long tail of high values)"
            elif skewness < -1:
                shape = "is highly left-skewed (most values are clustered on the higher end, with a long tail of low values)"
            elif skewness > 0.5:
                shape = "is slightly right-skewed"
            elif skewness < -0.5:
                shape = "is slightly left-skewed"
            else:
                shape = "is relatively symmetric (bell-shaped)"

            explanation = (
                f"Analysis of '{col}': The data ranges from a minimum of {minimum:g} to a maximum of {maximum:g}. "
                f"The average (mean) is {mean:g}, while the middle value (median) is {median:g}. "
                f"Overall, the distribution {shape}."
            )
        else:
            explanation = f"Analysis of '{col}': The column contains no valid numeric data to analyze."
        
        results.append({
            "path": path,
            "column": col,
            "explanation": explanation
        })

    return results

def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    if corr.empty:
        return None

    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    path="static/outputs/correlation.png"
    plt.savefig(path)
    plt.close()
    explanation = "Correlation Analysis: "
    import numpy as np
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    upper_tri = corr.where(mask)
    
    insights = []
    if (upper_tri > 0).any().any():
        max_val = upper_tri.max().max()
        if max_val > 0.5:
            idx = np.where(upper_tri == max_val)
            col1 = upper_tri.index[idx[0][0]]
            col2 = upper_tri.columns[idx[1][0]]
            insights.append(f"Strongest positive relationship is between '{col1}' and '{col2}' ({max_val:.2f}).")
            
    if (upper_tri < 0).any().any():
        min_val = upper_tri.min().min()
        if min_val < -0.5:
            idx = np.where(upper_tri == min_val)
            col1 = upper_tri.index[idx[0][0]]
            col2 = upper_tri.columns[idx[1][0]]
            insights.append(f"Strongest negative relationship is between '{col1}' and '{col2}' ({min_val:.2f}).")

    if insights:
        explanation += " ".join(insights) + " These variables highly influence each other. A positive relationship means when one goes up, the other tends to go up. A negative relationship means when one goes up, the other tends to go down."
    else:
        explanation += "There are no exceptionally strong relationships (above 0.5 or below -0.5) between the numeric variables in this dataset."
    
    return {
        "path": path,
        "explanation": explanation
    }