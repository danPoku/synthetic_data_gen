import matplotlib.pyplot as plt
import pandas as pd

def save_to_csv(df, filename):
    """_summary_

    Args:
        df (DataFrame): A DataFrame containing the data to be saved.
        filename (str): The name of the file to save the DataFrame to.
    """
    df.to_csv(filename, index=False)

def preview_data(df, n=10):
    return df.head(n)

def plot_monthly_trends(df, diagnosis):
    """_summary_

    Args:
        df (DataFrame): A DataFrame containing the data to be plotted.
        diagnosis (str): The diagnosis for which to plot the monthly trend.
    """
    df_diag = df[df['primary_diagnosis'] == diagnosis]
    df_diag.index = pd.to_datetime(df_diag['datetime'])
    monthly_cases = df_diag.resample('M').sum()['number_of_cases']
    monthly_cases.plot(title=f'Monthly Trend for {diagnosis}')
    plt.xlabel('Month')
    plt.ylabel('Cases')
    plt.show()