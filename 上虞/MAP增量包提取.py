# coding:utf-8
from __future__ import unicode_literals
import os

import arcpy

workspace = r"F:\2023\Nov\上虞电子地图\test\map增量包.gdb"

arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    print(feature_class)
    fc = os.path.join(workspace, feature_class)
    if feature_class == "POI":
        with arcpy.da.UpdateCursor(fc, "UPDATETIME") as cursor:
            for row in cursor:
                if row[0] < '20230101':
                    cursor.deleteRow()
        continue
    with arcpy.da.UpdateCursor(fc, "UPDATESTATUS") as cursor:
        for row in cursor:
            if row[0] == "O":
                cursor.deleteRow()

print('done')


