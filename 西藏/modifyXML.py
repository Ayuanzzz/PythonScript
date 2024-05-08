import pandas as pd
import os
import xml.etree.ElementTree as ET

# folder_path = r"D:\Python\test\xml2\test"
folder_path = input("xml路径: ")
# file_path = r"D:\Python\test\xml2\移XML.xlsx"
file_path = input("excel路径：")
sheet_name = "Sheet1"  # 替换为你的表单名称


def modifySingleXML(xml_file_path, y, x, z):
    basename = os.path.basename(xml_file_path)
    dirname = os.path.dirname(xml_file_path)
    new_xml_path = "m_" + basename
    new_xml_path = os.path.join(dirname, new_xml_path)
    # 解析 XML 文件
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    # 获取特定元素的值
    specific_element = root.find("SRSOrigin")
    if specific_element is not None:
        original_string = specific_element.text
        xyz_list = [float(x) for x in original_string.split(",")]
        # print(xyz_list)
        x_coord = str(xyz_list[0] + y)
        y_coord = str(xyz_list[1] + x)
        z_coord = str(xyz_list[2] + z)
        new_xyz = f"{x_coord},{y_coord},{z_coord}"
        # print(new_xyz)
        # 替换特定元素的文本内容
        specific_element.text = new_xyz
        # 保存修改后的 XML 文件
        tree.write(new_xml_path, encoding="utf-8", xml_declaration=True)


# 使用 pandas 读取 Excel 文件
df = pd.read_excel(file_path, sheet_name=sheet_name)
# 按行迭代 DataFrame
for index, row in df.iterrows():
    try:
        # 对每一行执行操作
        # print(f"行索引: {index}, 数据: {df.iloc[index, 0]},{df.iloc[index, 1]},{df.iloc[index, 2]},{df.iloc[index, 3]}")
        xml_folder_path = os.path.join(folder_path, df.iloc[index, 0])
        print(xml_folder_path)
        if not os.path.exists(xml_folder_path):
            print(f"{xml_folder_path} not exists")
            continue
        for xmlname in os.listdir(xml_folder_path):
            if xmlname.endswith(".xml"):
                old_xml_path = os.path.join(xml_folder_path, xmlname)
                moveY = df.iloc[index, 1]
                moveX = df.iloc[index, 2]
                moveZ = df.iloc[index, 3]
                modifySingleXML(old_xml_path, moveY, moveX, moveZ)
    except Exception as e:
        # 处理其他类型的异常
        print(f"发生其他异常：{e}")

print("\nDone")
input("exit")
