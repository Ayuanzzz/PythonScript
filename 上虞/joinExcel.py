import pandas as pd
import json

map_excel = r"D:\Python\test\syxlsx\mapCode.xlsx"
dlg_excel = r"D:\Python\test\syxlsx\dlgCode.xlsx"
# 读取两个Excel文件为不同的DataFrame
df1 = pd.read_excel(map_excel)
df2 = pd.read_excel(dlg_excel)

# 基于某列连接（类似于SQL INNER JOIN）
# combined_df = df1.merge(df2, on='code', how='left')
combined_df = pd.merge(df1, df2, on='code')
print(combined_df)

# 将DataFrame保存为txt文件，使用逗号分隔
combined_df.to_csv(r"D:\Python\test\syxlsx\output.txt", sep='\t', index=False)

# # 转换为JSON对象列表
# json_list = combined_df.to_dict(orient='records')
#
# # 将JSON对象列表写入文件
# with open(r"D:\Python\test\syxlsx\jsontmp.json", 'w') as json_file:
#     json.dump(json_list, json_file, indent=4)
