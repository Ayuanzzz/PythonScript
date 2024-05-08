# coding:utf-8
from __future__ import unicode_literals
import json
import os
import arcpy


def deleteNone(fc, mapcode):
    with arcpy.da.UpdateCursor(fc, ("FCODE", "FNAME")) as cursor:
        for row in cursor:
            if row[0] == str(mapcode) and row[1] is None:
                cursor.deleteRow()


if __name__ == "__main__":

    json_file = r"F:\2023\Nov\上虞电子地图\table\DeleteByName.json"

    with open(json_file, 'r') as file:
        data = json.load(file)

        for i in data:
            try:
                # 改改改
                out_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
                out_path = os.path.join(out_dir, i["map"])

                deleteNone(out_path, i["mapcode"])
            except Exception as e:
                print(e)

    print('\nDone')
