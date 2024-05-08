# coding:utf-8
from __future__ import unicode_literals
import arcpy
import os


def addNone(gdb_path, fc):
    with arcpy.da.UpdateCursor(gdb_path, fc) as cursor:
        for row in cursor:
            if row[0] == " " or row[0] == "":
                row[0] = None
                cursor.updateRow(row)


# 改改改
gdb_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"

arcpy.env.workspace = gdb_dir
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    print(feature_class)
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        print(field.name)
        if field.name == "DISPLAY":
            continue
        gdb_path = (os.path.join(gdb_dir, feature_class))
        addNone(gdb_path, field.name)
    print("----------------------------------------")

print("\nDone")
