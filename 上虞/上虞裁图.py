# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy

if __name__ == "__main__":
    # 自己的数据
    my_gdb = r"F:\2023\Nov\许奕涛小块\I上虞2023年2000DLG数据库.gdb\DLG_I"
    # 裁图后的数据
    clip_gdb = r"F:\2023\Nov\许奕涛小块\120.gdb\DLG_I"
    # 裁图面shp（需与自己的gdb投影一致）
    shp_path = r"F:\2023\Nov\许奕涛小块\zxlshp\外部边t.shp"

    arcpy.env.workspace = my_gdb
    feature_classes = arcpy.ListFeatureClasses()

    for feature_class in feature_classes:
        print(feature_class)
        try:
            my_path = os.path.join(my_gdb, feature_class)
            clip_path = os.path.join(clip_gdb, feature_class)
            arcpy.Clip_analysis(my_path, shp_path, clip_path)
        except Exception as e:
            print(e)

print('----------------------------------')
print("数据已裁剪至: " + clip_gdb)
