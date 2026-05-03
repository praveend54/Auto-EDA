def enhanced_summary(df):
    summary={}
    for col in df.columns:
        summary[col]={
            "dtype": str(df[col].dtype),
            "unique": df[col].unique(),
            "top_value": df[col].mode()[0] if not df[col].mode().empty else None
        }
    return summary