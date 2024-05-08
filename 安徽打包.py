import os
import shutil

source_folder = input("请输入文件夹路径: ")

destination_folder=source_folder+"PKG"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".xls"):
            file_name = file.replace(".xls", "")
            file_path = os.path.join(destination_folder, file_name)
            try:
                os.makedirs(file_path)
                print(file_path)
                xls_path = os.path.join(root, file_name+".xls")
                tif_path = os.path.join(root, file_name+".tif")
                tfw_path = os.path.join(root, file_name+".tfw")
                xls_new_path = os.path.join(file_path,file_name+".xls")
                tif_new_path = os.path.join(file_path,file_name+".tif")
                tfw_new_path = os.path.join(file_path,file_name+".tfw")
                shutil.move(xls_path,xls_new_path)
                shutil.move(tif_path,tif_new_path)
                shutil.move(tfw_path,tfw_new_path)
            except Exception as e:
                print(e)

print("\n运行完成")

input("按任意键退出")