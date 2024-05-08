# coding:utf-8
from __future__ import unicode_literals
import json
import os
import arcpy


def appendFeatures(oldPath, outPath, expression):
    arcpy.management.MakeFeatureLayer(oldPath, "tempLayer")
    try:
        arcpy.SelectLayerByAttribute_management("tempLayer", "NEW_SELECTION", where_clause=expression)
        arcpy.Append_management("tempLayer", outPath, "NO_TEST")
    finally:
        arcpy.Delete_management("tempLayer")


def updateValue(fc, field, dlgcode, mapcode):
    with arcpy.da.UpdateCursor(fc, field) as cursor:
        for row in cursor:
            if str(row[0]) == str(dlgcode):
                row[0] = str(mapcode)
                cursor.updateRow(row)


if __name__ == "__main__":

    json_file = r"F:\2023\Nov\上虞电子地图\table\mergeTable.json"

    with open(json_file, 'r') as file:
        data = json.load(file)

    for i in data:
        try:
            # 改改改
            # old_dir = r"F:\2023\Nov\上虞电子地图\test\source.gdb\DLG_I"
            old_dir = r"F:\2023\Nov\上虞电子地图\test\source.gdb"
            old_path = os.path.join(old_dir, i["dlg"])
            # print(old_path)

            # 改改改
            out_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
            out_path = os.path.join(out_dir, i["map"])
            # print(out_path)

            e = " FCODE = '{0}' ".format(i["dlgcode"])
            # print(e)
            appendFeatures(old_path, out_path, e)
            updateValue(out_path, "FCODE", i["dlgcode"], i["mapcode"])
            # print("-------------------------")
        except Exception as e:
            print(e)

print('\nDone')
