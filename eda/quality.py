def data_quality_score(df, missing, outliers, correlation):
    score = 100
    issues = []

    # 1. Missing values penalty
    total_missing = df.isnull().mean().mean() * 100
    if total_missing > 0:
        penalty = min(total_missing * 0.5, 30)
        score -= penalty
        issues.append(f"Missing data reduces quality by {penalty:.1f} points")

    # 2. Outliers penalty
    if outliers:
        avg_outliers = sum(outliers.values()) / len(outliers)
        penalty = min(avg_outliers * 0.3, 25)
        score -= penalty
        issues.append(f"Outliers reduce quality by {penalty:.1f} points")

    # 3. Correlation penalty (duplicate info)
    if correlation:
        penalty = min(len(correlation) * 2, 20)
        score -= penalty
        issues.append(f"Highly correlated features reduce quality by {penalty} points")

    # 4. Low variance columns
    low_variance = 0
    for col in df.select_dtypes(include='number'):
        if df[col].nunique() < 5:
            low_variance += 1

    if low_variance > 0:
        penalty = min(low_variance * 2, 10)
        score -= penalty
        issues.append(f"Low variance features reduce quality by {penalty} points")

    return round(max(score, 0), 2), issues