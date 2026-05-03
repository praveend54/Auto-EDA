import pandas as pd

def missing_values(df):
    total_rows = len(df)

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / total_rows) * 100

    result = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percent": missing_percent
    })

    # Only keep columns with missing values
    result = result[result["missing_count"] > 0]

    return result.sort_values(by="missing_percent", ascending=False)

def missing_analysis(df):
    insights = []

    for col in df.columns:
        pct = df[col].isnull().mean() * 100

        if pct == 0:
            continue
        elif pct < 10:
            insights.append(f"{col}: low missing values ({pct:.2f}%) → can fill easily")
        elif pct < 40:
            insights.append(f"{col}: moderate missing values ({pct:.2f}%) → needs careful imputation")
        elif pct < 70:
            insights.append(f"{col}: high missing values ({pct:.2f}%) → consider dropping or advanced methods")
        else:
            insights.append(f"{col}: very high missing values ({pct:.2f}%) → likely should be dropped")

    return insights