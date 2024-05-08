# coding:utf-8
from __future__ import unicode_literals
import arcpy
import os

gdb_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
gdb_path = (os.path.join(gdb_dir, "TRA_NET_LN"))

with arcpy.da.UpdateCursor(gdb_path, ("FCODE", "DISPLAY")) as cursor:
    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

print("\nDone")

