import matplotlib.pyplot as plt
import pandas as pd


def plot_trends(df, diagnosis, frequency, title_suffix, xlabel):
    """Plot the trend of cases for a specific diagnosis based on a given frequency.
    
    Args:
        df (DataFrame): The DataFrame containing the data.
        diagnosis (str): The diagnosis to filter the data by.
        frequency (str): The resampling frequency ('ME' for monthly, 'Y' for yearly, etc.).
        title_suffix (str): The suffix for the plot title.
        xlabel (str): The label for the x-axis.
    """
    df_diag = df[df['primary_diagnosis'] == diagnosis]
    df_diag.index = pd.to_datetime(df_diag['datetime'])
    cases = df_diag.resample(frequency).sum()['number_of_cases']
    cases.plot(title=f'{title_suffix} Trend for {diagnosis}')
    plt.xlabel(xlabel)
    plt.ylabel('Cases')
    plt.show()


def plot_monthly_trends(df, diagnosis):
    """Plot the monthly trend of cases for a specific diagnosis."""
    plot_trends(df, diagnosis, frequency='ME', title_suffix='Monthly', xlabel='Month')


def plot_yearly_trends(df, diagnosis):
    """Plot the yearly trend of cases for a specific diagnosis."""
    plot_trends(df, diagnosis, frequency='Y', title_suffix='Yearly', xlabel='Year')

def save_to_csv(df, filename):
    """Save the DataFrame to a CSV file.
    
    Args:
        df (DataFrame): The DataFrame to save.
        filename (str): The name of the file to save the DataFrame to.
    """
    df.to_csv(filename, index=False)
    print(f"DataFrame saved to {filename}")
    
def preview_data(df, num_rows=15):
    """Preview the first few rows of the DataFrame.
    
    Args:
        df (DataFrame): The DataFrame to preview.
        num_rows (int): The number of rows to preview.
    """
    print(df.head(num_rows))