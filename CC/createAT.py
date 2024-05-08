import os
import random
import sys
from pypinyin import pinyin, lazy_pinyin

import ccmasterkernel

photo_path = input("请输入影像路径: ").replace("\\", "/")
zh_str = os.path.basename(photo_path)

zh_py = ""
for i in lazy_pinyin(zh_str):
    zh_py += i
print(zh_py)

# projectDirPath = r"\\172.16.0.16\data70\xizang\jianggangsi"
projectDirPath = input("请输入项目路径: ").replace("\\", "/")
# projectName = "jgs2"
projectName = input("请输入项目名: ").replace("\\", "/")

# --------------------------------------------------------------------
# create project
# --------------------------------------------------------------------

project = ccmasterkernel.Project()
project.setName(projectName)
project.setDescription('Automatically generated from python script')
project_file_path = os.path.join(projectDirPath, projectName)
os.makedirs(project_file_path)
project_file_path_ccm = (project_file_path + ".ccm").replace("\\", "/")
print(project_file_path_ccm)
project.setProjectFilePath(project_file_path_ccm)

# job_path
job_list = ["33", "55", "44"]
choice = random.choice(job_list)
job_path = f"//172.16.0.{choice}/ccjobs/{projectName}"
print(job_path)
os.makedirs(job_path)
project.setJobQueuePath(job_path)

# save project
err = project.writeToFile()
if not err.isNone():
    print(err.message)
    sys.exit(0)

print('Project %s successfully created.' % projectName)
print('')

# --------------------------------------------------------------------
# create block
# --------------------------------------------------------------------
block = ccmasterkernel.Block(project)
project.addBlock(block)

block.setName('block #1')
block.setDescription('input block')
photogroups = block.getPhotogroups()

file_list = ["3倾斜", "1环绕", "2地面补拍"]

for name in file_list:
    photo_sub_folder = os.path.join(photo_path, name)
    print(photo_sub_folder)
    for i in os.listdir(photo_sub_folder):
        photo_sub_sub_folder = os.path.join(photo_sub_folder, i)
        print(photo_sub_sub_folder)
        files = os.listdir(photo_sub_sub_folder)

        for file in files:
            file = os.path.join(photo_sub_sub_folder, file)
            print(file)
            # add photo, create a new photogroup if needed
            lastPhoto = photogroups.addPhotoInAutoMode(file)

            if lastPhoto is None:
                print('Could not add photo %s.' % file)
                continue

            # upgrade block positioningLevel if a photo with position is found (GPS tag)
            if not lastPhoto.pose.center is None:
                block.setPositioningLevel(ccmasterkernel.PositioningLevel.PositioningLevel_georeferenced)

print('')

# save project
err = project.writeToFile()
if not err.isNone():
    print(err.message)
    sys.exit(0)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
print('\n')

print(photo_path)
print(project_file_path_ccm)
print(job_path)

input('exit')
