# Excel Report Automation using Python

This project automates the process of cleaning and summarizing messy Excel sales files using Python. It simulates a real-world scenario where monthly sales reports are received as raw Excel files with inconsistent formatting and missing values.

## What This Project Does

- Combines multiple raw Excel files into a unified dataset
- Cleans missing and invalid entries
- Calculates total amount spent per customer
- Outputs a clean Excel report with formatted headers
- Works with thousands of sales records

## Input Data

The `/data` folder contains synthetic sales files:
- `raw_sales_january.xlsx`
- `raw_sales_february.xlsx`

Each file includes:
- `Date`
- `Customer`
- `Product`
- `Quantity`
- `Unit Price`
- `Amount` (with some intentionally missing/invalid entries)

These datasets were generated using `generate_inputs.py` to simulate realistic data for testing automation scripts.

## Output

The script produces:
- `output/cleaned_summary_report.xlsx`

This file contains:
- A summary table of `Customer` vs. `Total Spent`
- Bold header formatting for presentation-ready output

## Tools Used

- **Python 3**
- **pandas** – Data cleaning and summarization
- **openpyxl** – Excel file formatting

## Project Structure

excel-report-automation/
├── data/ # Raw Excel files (input)
├── output/ # Cleaned Excel report (output)
├── generate_inputs.py # Script to create synthetic sales data
├── main.py # Automation script: read, clean, summarize, format
├── .gitignore
├── requirements.txt
└── README.md


## How to Run This Project

1. Install dependencies:
pip install -r requirements.txt


2. Run the main script:
python main.py


3. Output will be saved to:
/output/cleaned_summary_report.xlsx


