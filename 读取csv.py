import csv

csv_path = r"D:\Python\test\workTable\huhuproject.csv"
out_path = r"D:\Python\test\workTable\空三.txt"
# 打开 CSV 文件
with open(csv_path, 'r', newline='') as csvfile:
    # 创建 CSV 读取器
    csv_reader = csv.reader(csvfile)

    # 逐行读取 CSV 文件
    for row in csv_reader:
        if '空三' in row[0]:
            print(row[0])
            with open(out_path, 'a') as txtfile:
                txtfile.write(row[0]+'\n')
