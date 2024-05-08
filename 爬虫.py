import os

def process_txt_file(input_file, output_file):
    # 打开 txt 文件并读取内容
    with open(input_file, "r") as file:
        content = file.read()

    # 用逗号替换空格
    content = content.replace(" ", ",")

    # 将修改后的内容写回 txt 文件
    with open(output_file, "w") as file:
        file.write(content)

# 获取当前目录中所有 txt 文件的列表
txt_files = [f for f in os.listdir() if f.endswith('.txt')]

# 处理当前目录中的每个 txt 文件
for txt_file in txt_files:
    output_file = f"processed_{txt_file}"
    process_txt_file(txt_file, output_file)
