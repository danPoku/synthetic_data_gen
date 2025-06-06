from toolkit.assumptions import Assumptions

def disease_definitions():
    """
    Define diseases, baseline daily case counts, seasonal adjustment factors and long-term trends.

    Returns:
        tuple:
            - diagnoses (dict): baseline daily case counts for each diagnosis.
            - seasonal_weights (dict): monthly adjustments factors to depict seasonality.
            - trend_factors (dict): annual growth trends.
    """
    # Global assumptions
    cfg = Assumptions()
    copd = cfg.get_disease_assumption('COPD')
    
    # Diagnoses definition and baseline daily case counts (hard-coded)
    # TODO: replace hard-coded values with data from YAML file
    diagnoses = {
        "Upper Respiratory Tract Infection (J00–J06)": 300,
        "Pneumonia (J12–J18)": 50,
        "Bronchiolitis (J21)": 15,
        "Acute Bronchitis (J20)": 20,
        "Asthma (J45)": 30,
        "Influenza (J09–J11)": 5,
        "Chronic Obstructive Pulmonary Disease (J44)": 155
    }
    
    # Seasonal adjustment factors for each month (index 0 = January, 11 = December)
    # Monthly multipliers to indicate increase or decrease in disease incidence during that month.
    seasonal_weights = {
        "Upper Respiratory Tract Infection (J00–J06)": [1.3, 1.1, 0.8, 0.8, 1.0, 1.2, 1.0, 0.7, 0.8, 0.9, 1.0, 1.2],
        "Pneumonia (J12–J18)": [1.1, 1.0, 0.8, 0.9, 1.1, 1.3, 1.2, 1.0, 0.9, 0.8, 0.8, 1.0],
        "Bronchiolitis (J21)": [0.1, 0.1, 0.2, 0.4, 0.7, 1.0, 0.8, 0.5, 0.3, 0.2, 0.1, 0.1],
        "Acute Bronchitis (J20)": [1.2, 1.1, 0.9, 0.9, 1.0, 1.2, 1.1, 0.8, 0.9, 1.0, 1.0, 1.1],
        "Asthma (J45)": [1.3, 1.2, 1.0, 0.9, 1.0, 1.0, 0.9, 0.8, 0.9, 1.0, 1.1, 1.2],
        "Influenza (J09–J11)": [0.5, 0.5, 0.7, 0.8, 1.0, 1.3, 1.0, 0.7, 1.1, 0.9, 0.6, 0.5],
        "Chronic Obstructive Pulmonary Disease (J44)": [1.2, 1.1, 1.0, 1.0, 0.8, 0.9, 0.8, 0.9, 1.0, 1.1, 1.1, 1.2]
    }

    # Long-term trend factors per year for each diagnosis
    years = range(2015, 2025)  # From 2015 to 2024
    trend_factors = {
        "Upper Respiratory Tract Infection (J00–J06)": {yr: 1 + 0.07*(yr - 2015) for yr in years},
        "Pneumonia (J12–J18)": {yr: 1 + 0.03*(yr - 2015) for yr in years},
        "Bronchiolitis (J21)": {yr: 1.0 for yr in years},  # No trend assumed
        "Acute Bronchitis (J20)": {yr: 1 + 0.03*(yr - 2015) for yr in years},
        "Asthma (J45)": {yr: 1 + 0.05*(yr - 2015) for yr in years},
        "Influenza (J09–J11)": {yr: 1.0 for yr in years},
        "Chronic Obstructive Pulmonary Disease (J44)": {yr: 1 + 0.02*(yr - 2015) for yr in years}
    }
    
    # COPD from yaml
    key = "Chronic Obstructive Pulmonary Disease (J44)"
    diagnoses[key] = copd['baseline_daily_cases']
    # Values Jan, Feb, ..., Dec
    seasonal_weights[key] = list(copd['seasonal_weights'].values())
    trend_factors[key] = {int(y): f for y, f in copd['trend_factors'].items()}
    # Monthly distribution
    monthly_distribution = copd['monthly_distribution']
    
    return diagnoses, seasonal_weights, trend_factors, monthly_distribution