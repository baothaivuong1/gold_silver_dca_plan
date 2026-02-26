# Gold & Silver Investment Plan

A Python-based analysis tool for gold and silver investment strategies using Dollar Cost Averaging (DCA) and technical analysis across multiple timeframes.

## Features

- **Multi-timeframe Analysis**: Analyze gold and silver prices at daily, weekly, and monthly intervals
- **Data Processing**: Comprehensive data handling with CSV storage and retrieval
- **Dollar Cost Averaging (DCA)**: Implement and test DCA strategies
- **Jupyter Notebooks**: Interactive analysis and visualization notebooks

## Project Structure

```
.
├── data/                           # Price data directory
│   ├── daily/                     # Daily OHLCV data
│   │   ├── gold.csv
│   │   └── silver.csv
│   ├── weekly/                    # Weekly OHLCV data
│   │   ├── gold.csv
│   │   └── silver.csv
│   └── monthly/                   # Monthly OHLCV data
│       ├── gold.csv
│       └── silver.csv
├── notebooks/                      # Jupyter notebooks
│   ├── 1.get_data.ipynb           # Data acquisition and preparation
│   └── 2.test_on_different_timeframe.ipynb  # Multi-timeframe testing
├── dca.py                         # DCA strategy implementation
├── README.md                      # This file
├── LICENSE                        # MIT License
└── .gitignore                     # Git ignore rules
```

## Requirements

- Python 3.7+
- pandas
- numpy
- jupyter
- matplotlib (for visualization)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd gold_silver_plan
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Getting Data
Run the first notebook to fetch and prepare price data:
```bash
jupyter notebook notebooks/1.get_data.ipynb
```

### Testing Strategies
Test DCA and other strategies across different timeframes:
```bash
jupyter notebook notebooks/2.test_on_different_timeframe.ipynb
```

### Using DCA Module
Import and use the DCA strategy in your own code:
```python
from dca import DCA

# Initialize and run DCA strategy
strategy = DCA(data, parameters)
results = strategy.run()
```

## Data Format

CSV files contain historical price data with the following columns:
- Date
- Open
- High
- Low
- Close
- Volume

## Conclusion

### Fixed DCA Remains the Superior Strategy

Based on comprehensive testing across multiple timeframes (daily, weekly, and monthly) and market conditions (full period 2000-2026 and challenging period 2011-2018), the **Fixed Dollar Cost Averaging (DCA)** strategy consistently demonstrates its effectiveness as the most reliable investment approach.

#### Key Findings:

1. **Consistency Across Timeframes**: Fixed DCA maintains stable performance whether analyzed using daily, weekly, or monthly data intervals, indicating robust and predictable results regardless of data frequency.

2. **Resilience in Challenging Markets**: During the difficult 2011-2018 period (characterized by declining precious metal prices), Fixed DCA proved to be the most defensive strategy, protecting capital while maintaining steady accumulation.

3. **Simplicity & Reliability**: While alternative strategies like Value Averaging, Signal-Based RSI, Double Down, and Lump Sum Hybrid offer optimization potential, Fixed DCA's simplicity combined with consistent performance makes it the most practical choice for long-term investors.

4. **Long-term Value Accumulation**: Over the extended 2000-2026 period, the Fixed DCA strategy leveraged both bull and bear markets effectively, demonstrating that consistent, disciplined investing beats market timing.

#### Recommendation:

For precious metals investment (gold and silver), **Fixed DCA with regular monthly or weekly contributions** is the recommended strategy. It removes emotional decision-making, provides consistent market exposure, and has historically delivered superior risk-adjusted returns compared to other tested methodologies.

The data strongly supports that *time in the market* combined with *consistent contributions* beats *timing the market*, making Fixed DCA the most effective approach for long-term wealth building in precious metals.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created for investment analysis and strategy testing.
