import numpy as np
import pandas as pd
from .diseases import load_disease_definitions
from .temporal import apply_temporal_factors

class SyntheticDataGenerator:
    def __init__(self, location, start_date, end_date, seed=42):
        self.location = location
        self.dates = pd.date_range(start=start_date, end=end_date, freq='D')
        np.random.seed(seed)
        self.diseases, self.seasonal_weights, self.trend_factors = load_disease_definitions()

    def simulate(self):
        data_records = []
        for date in self.dates:
            day_factor = apply_temporal_factors(date)
            month_index = date.month - 1
            year = date.year

            for diag, base_rate in self.diseases.items():
                seasonal = self.seasonal_weights[diag][month_index]
                trend = self.trend_factors[diag][year]
                mean_cases = base_rate * seasonal * trend * day_factor

                count = np.random.poisson(mean_cases)

                if diag in ["Upper Respiratory Tract Infection (J00–J06)", "Pneumonia (J12–J18)"] and count < 1:
                    count = 1

                data_records.append({
                    "datetime": date.strftime("%Y-%m-%d"),
                    "city": self.location,
                    "primary_diagnosis": diag,
                    "number_of_cases": int(count)
                })

        return pd.DataFrame(data_records)