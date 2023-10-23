import xml.etree.ElementTree as ET
import os

# 读取jpg
file_names = []
dir_path = r"D:\Python\杂\JPG"
img_path = r"G:\testDem\Jpg"
for file_name in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_name)) and file_name.endswith(".JPG"):
        file_names.append(file_name)
        ImageFile = os.path.join(img_path, file_name)

with open('images.xml', 'w') as f:
    for i, file in enumerate(file_names):
        image_id = i
        image_file = os.path.join(img_path, file)
        camera_id = -1
        eoe_id = -1
        strip_id = 1
        photo_id = i + 1
        rotate_flag = 0
        # 将节点数据格式化为XML字符串，并在每个标签后添加换行符
        xml_str = '<ImageID>{}</ImageID>\n<ImageFile>{}</ImageFile>\n<CameraID>{}</CameraID>\n<EOEID>{}</EOEID>\n<StripID>{}</StripID>\n<PhotoID>{}</PhotoID>\n<RotateFlag>{}</RotateFlag>\n'.format(
            image_id, image_file, camera_id, eoe_id, strip_id, photo_id, rotate_flag)
        # 写入文件
        f.write(xml_str)

print('提取完成，已生成images.xml')