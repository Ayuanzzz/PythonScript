from PIL import Image

# 打开图片文件
image = Image.open(r"C:\Users\admin\Desktop\2313750310005.JPG")

# 检查图像是否包含EXIF信息
if hasattr(image, "_getexif"):
    exif_info = image._getexif()

    if exif_info is not None:
        # 打印所有的EXIF标签和值
        for tag, value in exif_info.items():
            print(f"Tag: {tag}, Value: {value},Type{type(value)}")
    else:
        print("没有EXIF信息。")
else:
    print("该图像不包含EXIF信息。")
