# coding: utf-8

import shutil
import time
import os

originFile = r"D:\tmp\file\1.txt"
copyDir = r"D:\tmp\copyNew"


# 路径拼接
def joinPath(jpath, jfile):
    return "{jpath}\{jfile}".format(jpath=jpath, jfile=jfile)


# 创建文件夹
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


# 创建copy文件夹
mkdir(copyDir)

# 创建时间戳文件夹
t = time.time()
dirName = int(t)
timeDir = joinPath(copyDir, dirName)
mkdir(timeDir)

# 拷贝文件
copyName = os.path.basename(originFile)
copyFile = joinPath(timeDir, copyName)
shutil.copyfile(originFile, copyFile)

print(copyName+" 已拷贝")
