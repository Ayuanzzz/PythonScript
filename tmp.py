from aspose.cells import Workbook
import os

folder_path = r"D:\Python\test\tmp"

def xlsxToXls(xlsx_path):
    xls_path = xlsx_path.replace(".xlsx",".xls")
    workbook = Workbook(xlsx_path)
    workbook.save(xls_path)

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file == '建（构）筑物.xlsx':
            xlsx_file = os.path.join(root, file)
            print(xlsx_file)
            xlsxToXls(xlsx_file)
            os.remove(xlsx_file)
