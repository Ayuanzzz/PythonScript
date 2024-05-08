# coding:utf-8
from __future__ import unicode_literals
import json
import os
import arcpy


def updateValue(fc, f1, f2, code, fscale):
    with arcpy.da.UpdateCursor(fc, (f1, f2)) as cursor:
        for row in cursor:
            if str(row[0]) == str(code):
                row[1] = int(fscale)
                # print("{0}--{1}".format(row[0], row[1]))
                cursor.updateRow(row)


if __name__ == "__main__":

    json_file = r"F:\2023\Nov\上虞电子地图\table\FSCALE.json"

    with open(json_file, 'r') as file:
        data = json.load(file)

    for i in data:
        try:
            # 改改改
            out_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
            out_path = (os.path.join(out_dir, i["map"])).strip()
            # print(out_path)
            updateValue(out_path, "FCODE", "FSCALE", i["mapcode"], i["fscale"])
        except Exception as e:
            print(e)

print('\nDone')
