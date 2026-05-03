def correlation_analysis(df):
    corr = df.corr(numeric_only=True)
    high_corr = []
    if corr.empty:
        return high_corr

    for row in corr.index:
        for col in corr.columns:
            if col != row and abs(corr.loc[row, col]) > 0.8:
                high_corr.append((row, col, corr.loc[row, col]))
    return high_corr