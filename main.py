import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Load data into python
filepaths = glob.glob("invoices/*.xlsx")
# Load data into dataframes
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Create pdf file
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=18, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=18, txt=f"Date: {date}")

    pdf.output(f"PDFs/{filename}.pdf")
