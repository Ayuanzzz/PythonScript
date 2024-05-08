# coding:utf-8
from __future__ import unicode_literals
import arcpy
import os

# 改改改
workspace = r"F:\2023\Nov\上虞电子地图\test\source.gdb"

arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    if feature_class == 'ANNO_I':
        continue
    try:
        fc = os.path.join(workspace, feature_class)
        print(fc)
        with arcpy.da.UpdateCursor(fc, "FCODE") as cursor:
            for row in cursor:
                row[0] = row[0].replace(" ", "")
                cursor.updateRow(row)
    except Exception as e:
        print(e)

print('done')
