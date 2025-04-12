def load_disease_definitions():
    diagnoses = {
        "Upper Respiratory Tract Infection (J00–J06)": 300,
        "Pneumonia (J12–J18)": 50,
        "Bronchiolitis (J21)": 15,
        "Acute Bronchitis (J20)": 20,
        "Asthma (J45)": 30,
        "Influenza (J09–J11)": 5,
        "Chronic Obstructive Pulmonary Disease (J44)": 8
    }
    
    # Seasonal adjustment factors for each month (index 0 = January, 11 = December)
    seasonal_weights = {
        "Upper Respiratory Tract Infection (J00–J06)": [1.3, 1.1, 0.8, 0.8, 1.0, 1.2, 1.0, 0.7, 0.8, 0.9, 1.0, 1.2],
        "Pneumonia (J12–J18)": [1.1, 1.0, 0.8, 0.9, 1.1, 1.3, 1.2, 1.0, 0.9, 0.8, 0.8, 1.0],
        "Bronchiolitis (J21)": [0.1, 0.1, 0.2, 0.4, 0.7, 1.0, 0.8, 0.5, 0.3, 0.2, 0.1, 0.1],
        "Acute Bronchitis (J20)": [1.2, 1.1, 0.9, 0.9, 1.0, 1.2, 1.1, 0.8, 0.9, 1.0, 1.0, 1.1],
        "Asthma (J45)": [1.3, 1.2, 1.0, 0.9, 1.0, 1.0, 0.9, 0.8, 0.9, 1.0, 1.1, 1.2],
        "Influenza (J09–J11)": [0.5, 0.5, 0.7, 0.8, 1.0, 1.3, 1.0, 0.7, 1.1, 0.9, 0.6, 0.5],
        "Chronic Obstructive Pulmonary Disease (J44)": [1.2, 1.1, 1.0, 0.9, 0.8, 0.9, 0.8, 0.9, 1.0, 1.1, 1.1, 1.2]
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

    return diagnoses, seasonal_weights, trend_factors