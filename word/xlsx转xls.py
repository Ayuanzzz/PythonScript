import win32com.client as win32
import os

# folder_path = r"D:\Python\test\output"
folder_path = r"D:\Python\test\mOutput"


# 取消兼容性检查

def xlsxToXls(xls_file, xlsx_file):
    try:
        # 启动Excel应用程序
        excel = win32.gencache.EnsureDispatch("Excel.Application")
        excel.DisplayAlerts = False
        # 打开XLSX文件
        wb = excel.Workbooks.Open(os.path.abspath(xlsx_file))

        # 保存为XLS文件
        wb.SaveAs(os.path.abspath(xls_file), FileFormat=56)  # FileFormat=56表示XLS格式

        # 关闭工作簿
        wb.Close(SaveChanges=False)
    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        # 退出Excel应用程序
        excel.Application.Quit()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".xlsx"):
            xlsx_file = os.path.join(root, file)
            xls_file = xlsx_file.replace(".xlsx", ".xls")
            print(xls_file)
            print(xlsx_file)
            print("--------------------------------")
            xlsxToXls(xls_file, xlsx_file)
            os.remove(xlsx_file)

print("\nDone")
