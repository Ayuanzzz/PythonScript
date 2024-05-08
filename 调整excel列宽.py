import openpyxl
import os

folder_path = r"D:\Python\test\mOutput"


def adjustColumnWidth(excel_path):
    # 打开 Excel 文件
    workbook = openpyxl.load_workbook(excel_path)
    # 选择要调整列宽的工作表
    sheet = workbook.active
    # 遍历每一列并自适应列宽
    for column_cells in sheet.columns:
        max_length = 0
        column = column_cells[0].column_letter  # 获取列的字母标识符
        for cell in column_cells:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 10)
        sheet.column_dimensions[column].width = adjusted_width
    # 保存 Excel 文件
    workbook.save(excel_path)


for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.xlsx'):
            excel_path = os.path.join(root, file_name)
            print(excel_path)
            adjustColumnWidth(excel_path)

print("\nDone")
