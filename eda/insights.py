def generate_insights(df):
    insights = []

    for col in df.select_dtypes(include='number'):
        skew = df[col].skew()

        if skew > 1:
            insights.append(f"{col} is highly positively skewed")

        if skew < -1:
            insights.append(f"{col} is highly negatively skewed")

    return insights