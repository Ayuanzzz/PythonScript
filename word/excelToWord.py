import glob
import os
import sys

from aspose.cells import Workbook

# 指定要搜索的文件夹路径
folder_path = input("请输入Excel文件夹路径: ")  # 将此路径替换为您的文件夹路径

# 使用glob模块获取文件夹下所有xlsx文件的路径
xlsx_files = glob.glob(os.path.join(folder_path, "*.xlsx"))

def eToW(excel_file,word_file):
    workbook = Workbook(excel_file)
    workbook.save(word_file)

# 打印所有xlsx文件的路径
for excel_file in xlsx_files:
    print(f"\n转换--{excel_file}")
    word_file = excel_file.replace("xlsx","docx")
    try:
        eToW(excel_file, word_file)
    except Exception as e:
        # 捕获所有其他异常并打印异常信息
        print(f"发生了异常: {e}")

print("\n转换完成")

# 提示用户按任意键退出程序
print("按任意键退出程序...")

# 等待用户按下任意键后立即退出程序
input()
sys.exit()






