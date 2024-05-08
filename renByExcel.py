import os
import openpyxl

# folder_path=r"D:\Python\data\test2"
# excel_path="西藏活动场所编号.xlsx"
folder_path = input("请输入Word文件夹: ")
excel_path=input("请输入Excel路径：")

# 打开Excel文件
workbook = openpyxl.load_workbook(excel_path)

# 选择要读取的工作表
worksheet = workbook.active

# 获取B列和C列的所有单元格
column_B = worksheet['B']
column_C = worksheet['C']

# 从第二行开始遍历B列和C列数据并创建对象
data_objects = []

for cell_B, cell_C in zip(column_B[1:], column_C[1:]):
    cell_value_B = cell_B.value
    cell_value_C = cell_C.value

    if cell_value_B is not None and cell_value_C is not None:
        data_object = {
            'name': cell_value_B,
            'num': cell_value_C
        }
        data_objects.append(data_object)

# 关闭工作簿
workbook.close()

file_names = os.listdir(folder_path)
docx_paths = [os.path.join(folder_path, file) for file in file_names if file.endswith(".docx")]
for docx_path in docx_paths:
    print(docx_path)
    for data_object in data_objects:
        basename = os.path.basename(docx_path)
        temp_name = basename.replace("像片控制点点之记.docx", "")
        try:
            if temp_name in data_object['name']:
                new_name = str(data_object['num']) + basename
                new_docx_path = os.path.join(folder_path, new_name)
                os.rename(docx_path, new_docx_path)
        except Exception as e:
            # 处理其他类型的异常
            print(f"发生了未处理的异常: {e}")

print("\n修改完成")

input("\n按任意键退出")

