# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy

if __name__ == "__main__":
    # 自己的数据
    my_gdb = r"F:\2023\Nov\许奕涛小块\test\SYxxy.gdb\DLG_I"
    # 接边后的数据
    jb_gdb = r"F:\2023\Nov\许奕涛小块\test\XYT-sy3.gdb\DLG_I"

    arcpy.env.workspace = my_gdb
    feature_classes = arcpy.ListFeatureClasses()

    for feature_class in feature_classes:
        print(feature_class)
        try:
            my_path = os.path.join(my_gdb, feature_class)
            jb_path = os.path.join(jb_gdb, feature_class)
            arcpy.Append_management(jb_path, my_path, "NO_TEST")
        except Exception as e:
            print(e)

print('----------------------------')
print("数据已合并至: " + my_gdb)
