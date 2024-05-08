# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy


def appendFeatures(oldPath, outPath):
    arcpy.management.MakeFeatureLayer(oldPath, "tempLayer")
    try:
        arcpy.Append_management("tempLayer", outPath, "NO_TEST")
    finally:
        arcpy.Delete_management("tempLayer")


if __name__ == "__main__":
    # 改改改
    old_dir = r"F:\2023\Nov\上虞电子地图\地名地址\上虞成果\地名地址脱密变形前成果JWD.gdb"
    old_path = os.path.join(old_dir, "POI")
    print(old_path)

    # 改改改
    out_dir = r"F:\2023\Nov\上虞电子地图\test\map.gdb"
    out_path = os.path.join(out_dir, "POI")
    print(out_path)

    appendFeatures(old_path, out_path)
    print("-------------------------")

print('\nDone')
