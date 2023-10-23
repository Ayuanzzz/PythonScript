# coding: utf-8
import os
from openpyxl import load_workbook

folder_path = r"D:\TestData\excel"  # 替换为您要读取的文件夹路径

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):  # 只处理Excel文件
        file_path = os.path.join(folder_path, filename)
        workbook = load_workbook(filename=file_path)  # 加载Excel文件
        worksheet = workbook.active
        cell_value = worksheet["A1"].value  # 获取A1单元格的内容
        new_filename = cell_value + ".xlsx"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)  # 重命名文件

print("更名完成")
