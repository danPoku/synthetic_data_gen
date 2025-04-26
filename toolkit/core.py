import numpy as np
import pandas as pd
from toolkit.diseases import disease_definitions
from toolkit.temporal import temporal_factors


class SyntheticDataGenerator:
    """
    A class to generate synthetic healthcare data for a specified location and date range.
    Attributes:
        location (str): The name of the location for which data is generated.
        dates (pd.DatetimeIndex): A range of dates between the specified start and end dates.
        diseases (dict): A dictionary of disease names and their base rates.
        seasonal_weights (dict): A dictionary of seasonal adjustment factors for each disease.
        trend_factors (dict): A dictionary of yearly trend adjustment factors for each disease.
    Methods:
        __init__(location, start_date, end_date, seed=42):
            Initializes the SyntheticDataGenerator with location, date range, and random seed.
        simulate():
            Simulates synthetic healthcare data based on disease definitions, seasonal trends,
            and temporal factors, and returns the data as a pandas DataFrame.
    """
    def __init__(self, location, start_date, end_date, seed=42):
        self.location = location
        self.dates = pd.date_range(start=start_date, end=end_date, freq="D")
        np.random.seed(seed)
        self.diseases, self.seasonal_weights, self.trend_factors = disease_definitions()

    def simulate(self):
        """
        Simulates synthetic health data based on temporal, seasonal, and trend factors.
        This method generates a synthetic dataset of disease cases for a given location
        and time period. The number of cases is calculated using a combination of base
        rates, seasonal weights, trend factors, and temporal adjustments. The data is
        returned as a pandas DataFrame.
        Returns:
            pd.DataFrame: A DataFrame containing the simulated data with the following columns:
                - 'datetime': The date of the record in 'YYYY-MM-DD' format.
                - 'city': The location for which the data is simulated.
                - 'primary_diagnosis': The name of the disease/diagnosis.
                - 'number_of_cases': The simulated number of cases for the diagnosis.
        Notes:
            - For certain diseases (e.g., "Upper Respiratory Tract Infection (J00–J06)" 
              and "Pneumonia (J12–J18)"), the minimum number of cases is set to 1 if the 
              simulated count is less than 1.
            - The method assumes that the following attributes are defined in the class:
                - self.dates: A list of datetime objects representing the simulation dates.
                - self.diseases: A dictionary mapping disease names to their base rates.
                - self.seasonal_weights: A dictionary of seasonal weights for each disease.
                - self.trend_factors: A dictionary of trend factors for each disease by year.
                - self.location: The name of the location for the simulation.
        """
        data_records = []
        for date in self.dates:
            day_factor = temporal_factors(date)
            month_index = date.month - 1
            year = date.year

            for diag, base_rate in self.diseases.items():
                seasonal = self.seasonal_weights[diag][month_index]
                trend = self.trend_factors[diag][year]
                mean_cases = base_rate * seasonal * trend * day_factor

                count = np.random.poisson(mean_cases)

                if (
                    diag
                    in [
                        "Upper Respiratory Tract Infection (J00–J06)",
                        "Pneumonia (J12–J18)",
                    ]
                    and count < 1
                ):
                    count = 1

                data_records.append(
                    {
                        "datetime": date.strftime("%Y-%m-%d"),
                        "city": self.location,
                        "primary_diagnosis": diag,
                        "number_of_cases": int(count),
                    }
                )

        return pd.DataFrame(data_records)
