# coding:utf-8
from __future__ import unicode_literals
import json
import os
import arcpy


def appendFeatures(oldPath, outPath, expression, tempLayer):
    arcpy.management.MakeFeatureLayer(oldPath, tempLayer)
    try:
        arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", where_clause=expression)
        arcpy.Append_management(tempLayer, outPath, "NO_TEST")
    finally:
        arcpy.Delete_management(tempLayer)


if __name__ == "__main__":

    json_file = r"F:\2023\Nov\上虞电子地图\table\joinTable.json"

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

            e = "FCODE = '{0}'".format(i["code"])
            tempLayer = "temp{0}".format(i["code"])
            # print(e)
            # print(tempLayer)
            appendFeatures(old_path, out_path, str(e), str(tempLayer))
            # print("-------------------------")
        except Exception as e:
            print(e)

print('\nDone')
