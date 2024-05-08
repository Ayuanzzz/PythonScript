import pandas as pd
import os

# 读取原始Excel文件
input_excel = r"D:\Python\test\修改总表.xlsx"
output_path = r"D:\Python\test\mOutput"

df = pd.read_excel(input_excel)

# 遍历每一行，创建单独的Excel文件
for index, row in df.iterrows():
    # 创建新的DataFrame包含当前行
    new_df = pd.DataFrame([row])

    # 提取行中的某个唯一标识符，用于文件名（这里假设列名为 'ID'）
    identifier = row['图号']

    # 创建单独的Excel文件
    output_excel = f"{identifier}.xlsx"
    new_df.to_excel(os.path.join(output_path,output_excel), index=False)

    print(f"{output_excel}")

print("All files created successfully.")
