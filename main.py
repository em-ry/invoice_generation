import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Load data into python
filepaths = glob.glob("invoices/*.xlsx")
# Load data into dataframes
for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Create pdf file
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=18, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=0, h=18, txt=f"Date: {date}", ln=1)

    # Add a header
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [item.replace('_', ' ').title() for item in columns]
    pdf.set_font(family="Times", size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=10, txt=columns[0], border=1)
    pdf.cell(w=70, h=10, txt=columns[1], border=1)
    pdf.cell(w=32, h=10, txt=columns[2], border=1)
    pdf.cell(w=30, h=10, txt=columns[3], border=1)
    pdf.cell(w=30, h=10, txt=columns[4], border=1, ln=1)

    # Add rows to table
    for index, rows in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=10, txt=str(rows['product_id']), border=1)
        pdf.cell(w=70, h=10, txt=str(rows['product_name']), border=1)
        pdf.cell(w=32, h=10, txt=str(rows['amount_purchased']), border=1)
        pdf.cell(w=30, h=10, txt=str(rows['price_per_unit']), border=1)
        pdf.cell(w=30, h=10, txt=str(rows['total_price']), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
