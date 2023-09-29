import pandas
import pandas as pd
import glob

# Load data into python
filepaths = glob.glob("invoices/*.xlsx")
# Load data into dataframes
for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
