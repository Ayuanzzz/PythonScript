# coding: utf-8
import glob
import os
import re

import docx

#更名
def reName(path):
    # 获取文件名
    file_name = os.path.basename(path)
    # 打开Word文档
    doc = docx.Document(path)
    # 原始文件名
    old_file_name = file_name.replace(".docx", "_00.jpg")
    old_file_path = os.path.join(os.path.dirname(path), old_file_name)
    # 新文件名
    if matchNum(doc):
        new_file_name = matchNum(doc) + ".jpg"
    else:
        new_file_name = old_file_name + "未匹配" + ".jpg"
    new_file_path = os.path.join(os.path.dirname(path), new_file_name)
    # 修改文件名
    os.rename(old_file_path, new_file_path)


# 匹配编码
def matchNum(doc):
    pattern = r'^3\d{10,}$'
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                match = re.search(pattern, cell.text)
                if match:
                    print('匹配到编码', match.group(0))
                    return match.group(0)

# 设置文件夹路径
folder_path = r"D:\Python\data\金府名门使用登记表（word-jpg-pdf）\金府名门使用登记表（word-jpg-pdf）"

# 获取文件夹下所有docx文件的路径列表
docx_files = glob.glob(os.path.join(folder_path, "*.docx"))

# 打印每个docx文件的路径
for file_path in docx_files:
    reName(file_path)
