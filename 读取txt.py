txt_path = r"D:\Python\test\workTable\空三2.txt"
new_txt_path = r"D:\Python\test\workTable\空三3.txt"

# 打开文本文件以读取数据
with open(txt_path, 'r') as txtfile:
    # 逐行读取文件内容
    lines = txtfile.readlines()

str_list = []
# 处理读取到的数据
for line in lines:
    str_list.append(line.strip())

print(str_list)
unique_list = list(set(str_list))
print(unique_list)

for line in unique_list:
    print(line)
    with open(new_txt_path, 'a') as txtfile:
        txtfile.write(line + '\n')
