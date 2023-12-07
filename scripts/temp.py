# bulk import data (data prepared in jupyter notebook)
''' 
Command to run this script:
pip install django-extensions
python manage.py runscript temp -v2

'''

from api.models import Company
import pandas as pd

def read_excel_and_output(file_path, num_rows=10):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, skiprows=1)

        # Output the first 10 rows
        #print(df.head(num_rows))

        return df
    except Exception as e:
        print(f"An error occurred: {e}")

def addCompany(df):
    companies = [
        Company(
            SP_ENTITY_NAME=row['SP_ENTITY_NAME'],
            SP_ENTITY_ID=row['SP_ENTITY_ID'],
            SP_EXCHANGE_TICKER=row['SP_EXCHANGE_TICKER'],
            IQ_INDUSTRY_CLASSIFICATION=row['IQ_INDUSTRY_CLASSIFICATION'],
            IQ_SECTOR=row['IQ_SECTOR'],
            IQ_INDUSTRY_GROUP=row['IQ_INDUSTRY_GROUP'],
            IQ_INDUSTRY=row['IQ_INDUSTRY'],
            IQ_PRIMARY_INDUSTRY=row['IQ_PRIMARY_INDUSTRY'],
            SP_GEOGRAPHY=row['SP_GEOGRAPHY'],
            SP_COUNTRY_NAME=row['SP_COUNTRY_NAME'],
        )
        for _, row in df.iterrows()
    ]

    Company.objects.bulk_create(companies)

def deleteCompany():
    Company.objects.all().delete()


def run():
    # deleteCompany()
    df = read_excel_and_output("scripts\SPGlobal_Export_US+HK_listed.xlsx")
    addCompany(df)