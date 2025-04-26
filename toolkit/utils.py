import matplotlib.pyplot as plt
import pandas as pd


def plot_monthly_trends(df, diagnosis):
    """Plot the monthly trend of cases for a specific diagnosis.
    This function filters the DataFrame for the specified diagnosis, converts the 'datetime' column to a datetime index,
    and plots the monthly trend of cases.

    Args:
        df (DataFrame): The DataFrame containing the data.
        diagnosis (str): The diagnosis to filter the data by.
    """
    df_diag = df[df['primary_diagnosis'] == diagnosis]
    df_diag.index = pd.to_datetime(df_diag['datetime'])
    monthly_cases = df_diag.resample('ME').sum()['number_of_cases']
    monthly_cases.plot(title=f'Monthly Trend for {diagnosis}')
    plt.xlabel('Month')
    plt.ylabel('Cases')
    plt.show()
    
def plot_yearly_trends(df, diagnosis):
    """Plot the yearly trend of cases for a specific diagnosis.
    This function filters the DataFrame for the specified diagnosis, converts the 'datetime' column to a datetime index,
    and plots the yearly trend of cases.
    
    Args:
        df (DataFrame): The DataFrame containing the data.
        diagnosis (str): The diagnosis to filter the data by.
    """
    df_diag = df[df['primary_diagnosis'] == diagnosis]
    df_diag.index = pd.to_datetime(df_diag['datetime'])
    yearly_cases = df_diag.resample('Y').sum()['number_of_cases']
    yearly_cases.plot(title=f'Yearly Trend for {diagnosis}')
    plt.xlabel('Year')
    plt.ylabel('Cases')
    plt.show()