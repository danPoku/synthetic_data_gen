import yaml
import os

class Assumptions:
    """
    Loads and provides access to synthetic data assumptions from YAML.
    """
    def __init__(self, path=None):
        if path is None:
            root = os.path.dirname(__file__)
            path = os.path.join(root, os.pardir, 'assumptions.yaml')
        with open(path, 'r', encoding='utf-8') as f:
            self._data = yaml.safe_load(f)

    def get_metadata(self):
        """Return metadata section"""
        return self._data.get('metadata', {})

    def get_disease_assumption(self, disease_key):
        """Return assumptions for a specific disease"""
        return self._data.get(disease_key, {})

    def get_baseline(self, disease_key):
        """Return baseline daily cases for disease"""
        return self.get_disease_assumption(disease_key).get('baseline_daily_cases')

    def get_seasonal_weights(self, disease_key):
        """Return monthly seasonal weights dict"""
        return self.get_disease_assumption(disease_key).get('seasonal_weights', {})

    def get_monthly_distribution(self, disease_key):
        """Return monthly distribution dict"""
        return self.get_disease_assumption(disease_key).get('monthly_distribution', {})

    def get_trend_factors(self, disease_key):
        """Return yearly trend factors dict"""
        return self.get_disease_assumption(disease_key).get('trend_factors', {})

    def get_urban_proportion(self, disease_key):
        """Return urban proportion for disease estimation"""
        return self.get_disease_assumption(disease_key).get('urban_proportion')
