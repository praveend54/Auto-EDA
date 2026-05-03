import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(df):
    paths = []

    for col in df.select_dtypes(include='number'):
        plt.figure()
        df[col].hist()
        path=f"static/outputs/{col}_hist.png"
        plt.savefig(path)
        plt.close()
        paths.append(path)

    return paths

def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    if corr.empty:
        return None

    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    path="static/outputs/correlation.png"
    plt.savefig(path)
    plt.close()
    return path