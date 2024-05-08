# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy

# 改改改
# gdb_path = r"F:\2023\Nov\上虞电子地图\test\source.gdb\DLG_I"
gdb_path = r"F:\2023\Nov\上虞电子地图\test\source.gdb"

arcpy.env.workspace = gdb_path

feature_classes = arcpy.ListFeatureClasses()

for fc in feature_classes:
    if fc == 'ANNO_I':
        continue
    print(fc)

    try:
        arcpy.AddField_management(fc, "UPDATETIME", "TEXT")
        arcpy.AddField_management(fc, "UPDATESTATUS", "TEXT")
        field_list = [field.name for field in arcpy.ListFields(fc)]

        if "last_edited_user" in field_list:
            with arcpy.da.UpdateCursor(fc, ("UPDATETIME", "last_edited_user", "UPDATESTATUS")) as cursor:
                for row in cursor:
                    row[0] = "20231112"
                    if row[1]:
                        row[2] = "U"
                    else:
                        row[2] = "O"
                    cursor.updateRow(row)
        if "last_edited_user" not in field_list:
            with arcpy.da.UpdateCursor(fc, ("UPDATETIME", "UPDATESTATUS")) as cursor:
                for row in cursor:
                    row[0] = "20231112"
                    row[1] = "O"
                    cursor.updateRow(row)
        if "ORIENTATION" in field_list:
            arcpy.AddField_management(fc, "FANGLE", "Double")
            with arcpy.da.UpdateCursor(fc, ("ORIENTATION", "FANGLE")) as cursor:
                for row in cursor:
                    row[1] = row[0]
                    cursor.updateRow(row)
        elif "NAME" in field_list:
            arcpy.AddField_management(fc, "FNAME", "TEXT")
            with arcpy.da.UpdateCursor(fc, ("NAME", "FNAME")) as cursor:
                for row in cursor:
                    row[1] = row[0]
                    cursor.updateRow(row)
    except Exception as e:
        print(e)

print("\nDone")
