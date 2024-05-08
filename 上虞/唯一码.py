# -*- coding:utf-8 -*-
import arcpy
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import uuid

if __name__ == '__main__':
    arcpy.env.workspace = r"F:\2023\Dec\uuid\I上虞区2022DLG数据库.gdb\DLG_I"
    workspace = arcpy.env.workspace
    fcs = arcpy.ListFeatureClasses()
    for fc in fcs:
        print(fc)
        if fc != 'ANNO_I':
            fds = arcpy.ListFields(fc)
            for fd in fds:
                fdName = fd.name
                if fdName.upper() == 'FEATUREID':
                    print ("\n更新图层" + fc + "字段FEATUREID开始")
                    aValue = (str(uuid.uuid1())).upper()
                    # print ('{0}.FEATUREID:{1}'.format(fc,aValue))
                    code_block = """def CalcUUID():
		aValue=(str(uuid.uuid1())).upper()
		return aValue"""
                    arcpy.CalculateField_management(in_table=fc, field=fdName, expression="CalcUUID()",
                                                    expression_type="PYTHON_9.3", code_block=code_block)
                    print ("更新图层" + fc + "字段FEATUREID唯一码完成")

                if fdName == 'UPDATEDATE':
                    print ("\n更新图层" + fc + "字段UPDATEDATE开始")
                    arcpy.CalculateField_management(fc, "UPDATEDATE", "'2023/10/29'", "PYTHON_9.3", "")
                    print ("更新图层" + fc + "字段UPDATEDATE完成")

                if fdName == 'FEATURESTATUS':
                    print ("\n更新图层" + fc + "字段FEATURESTATUS开始")
                    arcpy.CalculateField_management(fc, "FEATURESTATUS", "'-8888'", "PYTHON_9.3", "")
                    print ("更新图层" + fc + "字段FEATURESTATUS完成")

                if fdName == 'DATASOURCE':
                    print ("\n更新图层" + fc + "字段DATASOURCE开始")
                    arcpy.CalculateField_management(fc, "DATASOURCE", "'/'", "PYTHON_9.3", "")
                    print ("更新图层" + fc + "字段DATASOURCE完成")
        else:
            print ("\n不更新图层" + fc)
