# coding:utf-8
from __future__ import unicode_literals
import arcpy

# 改改改
workspace = r"F:\2023\Dec\上虞元数据重大要素\元数据模板\乐清市20221230DLG元数据.shp"

arcpy.env.workspace = workspace
feature_classes = arcpy.ListFeatureClasses()

for feature_class in feature_classes:
    print(feature_class)
    fields = arcpy.ListFields(feature_class)
    for field in fields:
        # print(field.name)
        # print(field.aliasName)
        # print(field.type)
        # print(field.length)
        print("{},{},{},{}".format(field.name, field.aliasName, field.type, field.length))
        print("------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++")
