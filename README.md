
# Data Processor Validator

This project validates the output of a Data Processor module that handles cricket player records from `.csv` and `.json` files.

## Features

- Reads and merges input from both `.csv` and `.json`.
- Filters and processes based on age, runs, wickets.
- Classifies players into types: All-Rounder, Batsman, Bowler.
- Splits output into `test.csv` and `odi.csv`.
- Validates outputs with test cases and schema checks.
- Includes CI pipeline with GitHub Actions.

## Setup

```bash
pip install -r requirements.txt
python src/data_processor.py
pytest --html=report.html
```
