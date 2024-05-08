# coding:utf-8
from __future__ import unicode_literals
import arcpy
import os

# 改改改
workspace = r"F:\2023\Nov\上虞电子地图\tmp\copyR.gdb"

arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    if feature_class == "RES_PY":
        try:
            print(feature_class)
            fc = os.path.join(workspace, feature_class)
            print(fc)
            # if feature_class == "POI":
            with arcpy.da.UpdateCursor(fc, "*") as cursor:
                for row in cursor:
                    cursor.deleteRow()
        except Exception as e:
            print(e)

print('done')
