import os

# 指定要搜索的文件夹路径
folder_path = r'D:\Python\test\已录寺庙YW1017'
a = []
# 使用os.listdir()列出文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file == '建（构）筑物.xlsx':
            file_path = os.path.join(root, file)
            a.append(file_path)

def joinExcel(filename):
    table_path = r'D:\Python\test\2121'
    # 使用os.listdir()列出文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(table_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_name == filename:
                print(os.path.join(root, file))

for file_path in a:
    # 使用os.path.split()函数分割文件路径
    directories = file_path.split(os.path.sep)

    # 获取倒数第二层目录
    if len(directories) >= 2:
        second_last_directory = directories[-2]
        # print(second_last_directory)
        temple_list = second_last_directory.split("基础")
        temple_name = temple_list[0]
        print(file_path)
        joinExcel(temple_name)
        print("--------------------------------")








