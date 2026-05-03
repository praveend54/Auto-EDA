def outlier_percentage(df):
    result={}
    for col in df.select_dtypes(include='number'):
        q1=df[col].quantile(0.25)
        q3=df[col].quantile(0.75)
        iqr=q3-q1
        outliers=((df[col]<q1-1.5*iqr) | (df[col]>q3+1.5*iqr))
        result[col]=(outliers.sum()/len(df))*100
    return result