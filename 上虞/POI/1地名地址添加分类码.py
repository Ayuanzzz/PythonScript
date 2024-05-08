# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy

# 改改改
gdb_path = r"F:\2023\Nov\上虞电子地图\地名地址\上虞成果\地名地址脱密变形前成果增量包JWD.gdb"

arcpy.env.workspace = gdb_path

feature_classes = arcpy.ListFeatureClasses()

for fc in feature_classes:
    if not fc == 'POI':
        continue
    print(fc)
    arcpy.AddField_management(fc, "FCODE", "TEXT")
    with arcpy.da.UpdateCursor(fc, ("FPOICODE", "FCODE")) as cursor:
        for row in cursor:
            row[1] = row[0]
            cursor.updateRow(row)

print("\nDone")
