from app.db.session import SessionLocal
from app.crud.crud_hospital import AddHospitalLocally
from app.utils import read_excel_data

def run_data_from_excel_sheet():
    sheet_list = [
        'karachi',
        'lahore',
        'islamabad_rawalpindi',
        'faisalabad',
        'peshawar',
        'multan',
        'hyderabad',
        'sukkur',
        'quetta',
        'gujranwala',
        'sargodha',
    ]
    for s in sheet_list:
        sheet_data = read_excel_data(
            file_path='app/tests/test_files/hospitals.xlsx',
            sheet_name=s,
            to_json=False
        )
        print(f'Loading data from sheet: {s}')
        AddHospitalLocally(SessionLocal()).add_scraping_hospitals(sheet_data)
        print(f'Finished loading data from sheet: {s}')
