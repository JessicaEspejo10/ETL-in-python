from datetime import datetime
import os

from base import session
from tables import PprCleanAll
import xlsxwriter
from sqlalchemy import text

# Settings
base_path = os.path.abspath(__file__ + "/../../")
ref_month = datetime.today().strftime("%Y-%m")

def export():
    data = session.execute(text('''SELECT * FROM insights''')).all()
    ref_month = datetime.today().strftime("%Y-%m")
    
    # Create the workbook
    workbook = xlsxwriter.Workbook(
        f"{base_path}\insights_export\InsightsExport_202102.xlsx"
    )
    
    # Add a new worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_column("B:G", 12)
    
    # Add the table with all results in the newly created worksheet
    worksheet.add_table(
        "B3:E20",
        {
            "data": data,
            "columns": [
                {"header": "County"},
                {"header": "Number of Sales 3 month"},
                {"header": "Tot sales 3 months"},
                {"header": "Max sales 3 months"},
                {"header": "Min sales 3 months"},
                {"header": "Avg sales 3 months"},
            ],
        },
    )
    workbook.close()
    
    print("Data exported:", f"{base_path}/insights_export/InsightsExport_202102.xlsx")

# Main function called inside the execute.py script
def main():
    export()
