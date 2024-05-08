import pandas as pd
import json

# 读取Excel文件
excel_file = input('Excel: ')
df = pd.read_excel(excel_file)
print(df)
# 指定列名称
# df.columns = ['name', 'age', 'num']

# 转换为JSON对象列表
json_list = df.to_dict(orient='records')

# 将JSON对象列表写入文件
json_path = excel_file.replace('.xlsx', '.json')
with open(json_path, 'w') as json_file:
    json.dump(json_list, json_file, indent=4)

print('\nDone')
