
import os 
import glob
from openpyxl import Workbook

# Define the directory path
DIRECTORY_PATH = "/home/jj/shlomo/"

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
    find_pdf_and_write_xlsx(DIRECTORY_PATH)

if __name__=='__main__':
    main()