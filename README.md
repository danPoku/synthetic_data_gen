# Synthetic Data Toolkit for Epidemiology Analytics

A modular, configurable toolkit for generating realistic synthetic epidemiological time-series data.  
Originally demonstrated for respiratory diseases in Accra (2015–2024), this framework can be extended to any disease/location.

---

## 📦 Repository Structure

```
synthetic_data_toolkit/
├── README.md
├── setup.py
├── requirements.txt
├── assumptions.yaml
├── toolkit/
│   ├── __init__.py
│   ├── assumptions.py
│   ├── core.py
│   ├── diseases.py
│   ├── temporal.py
│   └── utils.py
└── examples/
    └── example_usage.ipynb
```

- **`assumptions.yaml`**  
  Centralized configuration of baseline rates, seasonal patterns, trends, and distributions.

- **`toolkit/assumptions.py`**  
  Loader class for `assumptions.yaml`.

- **`toolkit/diseases.py`**  
  Disease definitions that mix hard-coded and YAML-driven parameters.

- **`toolkit/temporal.py`**  
  Weekday/holiday adjustment factors.

- **`toolkit/core.py`**  
  `SyntheticDataGenerator` class: orchestrates date range, disease models, and Poisson sampling.

- **`toolkit/utils.py`**  
  Helpers for exporting, previewing, and plotting data.

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-org/synthetic_data_toolkit.git
cd synthetic_data_toolkit

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate.bat     # Windows

# 3. Install dependencies
pip install -r requirements.txt
# or to install as a package
pip install .
```

---

## 🔧 Usage

### 1. Load assumptions & parameters

```python
from toolkit.assumptions import Assumptions

config = Assumptions()
copd_cfg = config.get_disease_assumption("COPD")

print("COPD baseline daily cases:", copd_cfg["baseline_daily_cases"])
```

### 2. Generate synthetic data

```python
from toolkit.core import SyntheticDataGenerator
from toolkit.utils import save_to_csv, preview_data, plot_monthly_trends

# Initialize generator
gen = SyntheticDataGenerator(
    location="Accra",
    start_date="2015-01-01",
    end_date="2024-12-31"
)

# Simulate
df = gen.simulate()

# Export
save_to_csv(df, "respiratory_cases_accra.csv")

# Quick preview
preview_data(df, n=10)

# Plot an example disease
plot_monthly_trends(df, "Asthma (J45)")
```

---

## ⚙️ Configuration (`assumptions.yaml`)

- **`baseline_daily_cases`**: Neutral per-day rate before seasonality/trends  
- **`seasonal_weights`**: Month-by-month multipliers  
- **`monthly_distribution`**: Fraction of annual total in each month  
- **`trend_factors`**: Year-by-year scaling factors  
- **`urban_proportion`**: Subnational scaling (e.g. Accra vs Ghana)

Edit `assumptions.yaml` and update `metadata.last_updated` whenever you change assumptions.

---

## 🧪 Testing & Validation

- **Unit tests** should verify:  
  - Sum of `monthly_distribution` ≈ 1.0  
  - Year keys in `trend_factors` cover your date range  
  - Seasonal weights list length == 12  

- **Data inspection**:  
  Run the example notebook and visually inspect seasonal and trend patterns.

---

## 📈 Extending to New Diseases

1. **Add a section** in `assumptions.yaml` (e.g. `"Influenza A"`)  
2. **Retrieve** via `config.get_disease_assumption("<KEY>")` in `diseases.py`  
3. **Regenerate** using the core generator

---

## 📜 License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.

> _Synthetic data is not a substitute for real observations. Use responsibly._