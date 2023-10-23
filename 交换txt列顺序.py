import os

folder_path = u'D:\Python\杂'  # 文件夹路径


def exchangCol(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    with open(path, 'w') as f:
        for line in lines:
            cols = line.split()  # 按空格分割每一行为列表
            cols[1], cols[2] = cols[2], cols[1]  # 交换第二列和第三列
            new_line = ','.join(cols) + '\n'  # 重新组合每一行
            f.write(new_line)
    print('正向交换列完成')


for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith('.txt'):
            file_path = os.path.join(dirpath, filename)
            print(file_path)
            exchangCol(file_path)
