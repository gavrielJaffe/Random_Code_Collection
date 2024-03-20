import os 
import sys
import glob
from openpyxl import Workbook

def write_pdf_list_to_excel(pdf_list, output_file):
    # Create a new Workbook
    wb = Workbook()
    # Select the active worksheet
    ws = wb.active
    # Write PDF file names to the Excel file
    for index, pdf_name in enumerate(pdf_list, start=1):
        ws[f'A{index}'] = pdf_name
    # Save the Excel file
    wb.save(output_file)
    print("Excel file created successfully at:", output_file)

def find_pdf_and_write_xlsx(directory):
    os.chdir(directory)  # Change to the specified directory
    pdf_files = (glob.glob("*.pdf"))
    pdf_list_without_extension = [file.replace('.pdf', '') for file in pdf_files]
    output_file = 'pdf_file_numbers.xlsx'
    write_pdf_list_to_excel(pdf_list_without_extension, output_file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py directory_path")
        return
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: Specified directory does not exist.")
        return
    find_pdf_and_write_xlsx(directory)

if __name__=='__main__':
    main()
