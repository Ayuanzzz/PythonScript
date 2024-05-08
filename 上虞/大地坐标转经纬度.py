# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import os
import arcpy


def convertCoord(gdb_path, output_gdb_path):
    arcpy.env.workspace = gdb_path
    feature_classes = arcpy.ListFeatureClasses()
    for feature_classe in feature_classes:
        print(feature_classe)
        in_dataset = os.path.join(gdb_path, feature_classe)
        out_dataset = os.path.join(output_gdb_path, feature_classe)
        out_coor = arcpy.SpatialReference(4490)
        arcpy.Project_management(in_dataset, out_dataset, out_coor)


# gdb文件夹路径
gdb_path = r"F:\2023\Nov\上虞电子地图\转经纬度\origin.gdb"

output_gdb_path = r"F:\2023\Nov\上虞电子地图\转经纬度\JWD.gdb"

convertCoord(gdb_path, output_gdb_path)

print("\nDone")
