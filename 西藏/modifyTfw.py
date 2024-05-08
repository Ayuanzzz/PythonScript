import os
import pandas as pd

folder_path = input("XML folder :")
# folder_path = r"D:\Python\test\modifyXML"
# file_path = r"D:\Python\test\modifyXML\周秀兰.xlsx"
file_path = input("Xlsx file :")
sheet_name = "Sheet1"

def modifySingleTfw(tfw_file_path, moveY, moveX):
    basename = os.path.basename(tfw_file_path)
    dirname = os.path.dirname(tfw_file_path)
    new_tfw_name = "m_" + basename
    new_tfw_path = os.path.join(dirname, new_tfw_name)
    try:
        with open(tfw_file_path, 'r') as tfw_file:
            # 读取 TFW 文件中的参数
            parameters = [float(line.strip()) for line in tfw_file]
            ori = parameters[:len(parameters) - 2]
            with open(new_tfw_path, 'w') as new_tfw_file:
                for i in ori:
                    new_tfw_file.write(f"{i}\n")
                new_tfw_file.write(f"{parameters[len(parameters) - 2] + moveY}\n")
                new_tfw_file.write(f"{parameters[len(parameters) - 1] + moveX}\n")

    except Exception as e:
        print(f"在读取 TFW 文件时发生错误：{e}")


# 使用 pandas 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name=sheet_name)
# 按行迭代 DataFrame
for index, row in df.iterrows():
    # 对每一行执行操作
    temple_folder_path = os.path.join(folder_path, df.iloc[index, 0])
    if not os.path.exists(temple_folder_path):
        print(f"{temple_folder_path} not exists")
        continue
    else:
        print(f"{temple_folder_path}")
    for tfwname in os.listdir(temple_folder_path):
        if tfwname.endswith(".tfw"):
            tfw_path = os.path.join(temple_folder_path, tfwname)
            moveY=df.iloc[index, 1]
            moveX=df.iloc[index, 2]
            modifySingleTfw(tfw_path,moveY,moveX)

print("\nDone")

input("exit")