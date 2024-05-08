# coding:utf-8
from __future__ import unicode_literals
import os

import arcpy

# workspace = r"F:\2023\Nov\上虞电子地图\库数据增量包.gdb\DLG_I"
workspace = r"F:\2023\Nov\上虞增量数据\库数据增量包.gdb"


arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    print(feature_class)
    try:
        fc = os.path.join(workspace, feature_class)
        with arcpy.da.UpdateCursor(fc, ("created_user", "last_edited_user")) as cursor:
            for row in cursor:
                if row[0] is None and row[1] is None:
                    cursor.deleteRow()
    except Exception as e:
        print(e)

print('done')
