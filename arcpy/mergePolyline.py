# coding:utf-8
import arcpy

# 设置工作空间和数据源
arcpy.env.workspace = r"D:\TestData"
input_layer = "tmp.shp"

# 扫描输入图层中的每条线段
with arcpy.da.UpdateCursor(input_layer, ["SHAPE@", "Name"]) as cursor:
    for row in cursor:
        # 获取当前线段的属性值
        attribute_value = row[1]

        # 定义查询语句，查找所有与当前线段属性值相同的线段
        query = "Name = '{0}'".format(attribute_value)
        related_lines = [related_row[0] for related_row in
                         arcpy.da.SearchCursor(input_layer, ["Name"], where_clause=query)]

        if related_lines:
            # 合并相关线段
            merged_line = row[0]
            for line in related_lines:
                merged_line = merged_line.union(line)

            # 更新当前线段的形状
            row[0] = merged_line
            cursor.updateRow(row)
