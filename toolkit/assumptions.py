import yaml
import os

class Assumptions:
    """
    Loads and provides access to synthetic data assumptions from YAML.
    """
    def __init__(self, path=None):
        if path is None:
            here = os.path.dirname(__file__)
            # Go up two levels to find the root directory
            project_root = os.path.abspath(os.path.join(here, os.pardir, os.pardir))
            path = os.path.join(project_root, 'config', 'assumptions.yaml')
        with open(path, 'r', encoding='utf-8') as f:
            self._data = yaml.safe_load(f)

    def get_metadata(self) -> dict:
        """Return metadata section"""
        return self._data.get('metadata', {})

    def get_disease_assumption(self, disease_key) -> dict:
        """Return assumptions for a specific disease"""
        return self._data.get(disease_key, {})

    def get_baseline(self, disease_key) -> int:
        """Return baseline daily cases for disease"""
        return self.get_disease_assumption(disease_key).get('baseline_daily_cases', 0)

    def get_seasonal_weights(self, disease_key) -> dict:
        """Return monthly seasonal weights dict"""
        return self.get_disease_assumption(disease_key).get('seasonal_weights', {})

    def get_monthly_distribution(self, disease_key) -> dict[str, float]:
        """Return monthly distribution dict"""
        return self.get_disease_assumption(disease_key).get('monthly_distribution', {})

    def get_trend_factors(self, disease_key) -> dict[int, float]:
        """Return yearly trend factors dict"""
        return self.get_disease_assumption(disease_key).get('trend_factors', {})

    def get_urban_proportion(self, disease_key) -> float:
        """Return urban proportion for disease estimation"""
        return self.get_disease_assumption(disease_key).get('urban_proportion')
