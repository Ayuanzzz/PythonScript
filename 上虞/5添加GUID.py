# coding:utf-8
from __future__ import unicode_literals
import os
import arcpy
import uuid


def createGuid():
    random_uuid = uuid.uuid4()
    # print(random_uuid)
    formatted_uuid = '-'.join(
        [random_uuid.hex[:8], random_uuid.hex[8:12], random_uuid.hex[12:16], random_uuid.hex[16:20],
         random_uuid.hex[20:]])
    unique_code = formatted_uuid[:32]
    return unique_code

# 改改改
workspace = r"F:\电子地图数据脱密变形前成果.gdb"

arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    print(feature_class)
    fc = os.path.join(workspace,feature_class)
    if not feature_class == "ASST_LN" and not feature_class == "POI":
        with arcpy.da.UpdateCursor(fc, ("FEATUREGUID", "USOURCE")) as cursor:
            for row in cursor:
                guid = createGuid()
                row[0] = guid
                row[1] = "/"
                cursor.updateRow(row)
    else:
        with arcpy.da.UpdateCursor(fc, ("FEATUREGUID")) as cursor:
            for row in cursor:
                guid = createGuid()
                row[0] = guid
                cursor.updateRow(row)

print('done')
