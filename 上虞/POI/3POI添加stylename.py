# coding:utf-8
from __future__ import unicode_literals
import json
import os
import arcpy


def updateValue(fc, f1, f2, fcode, stylename):
    with arcpy.da.UpdateCursor(fc, (f1, f2)) as cursor:
        for row in cursor:
            if str(row[0]) == str(fcode).replace(" ", ""):
                row[1] = stylename.replace(" ", "")
                cursor.updateRow(row)


if __name__ == "__main__":

    json_file = r"F:\2023\Nov\上虞电子地图\table\stylename.json"

    with open(json_file, 'r') as file:
        data = json.load(file)

    for i in data:
        print(i["stylename"])
        print(i["fcode"])
        print("==========================")
        try:
            # 改改改
            out_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
            out_path = (os.path.join(out_dir, "POI")).strip()
            print(out_path)

            updateValue(out_path, "FCODE", "STYLENAME", i["fcode"], i["stylename"])
        except Exception as e:
            print(e)

print('\nDone')
