import win32com.client as win32
import os

folder_path = r"D:\Python\test\tmp2\output"

def xlsToXlsx(xls_file, xlsx_file):
    try:
        # 启动Excel应用程序
        excel = win32.gencache.EnsureDispatch("Excel.Application")

        # 打开XLS文件
        wb = excel.Workbooks.Open(os.path.abspath(xls_file))

        # 保存为XLSX文件
        wb.SaveAs(os.path.abspath(xlsx_file), FileFormat=51)  # FileFormat=51表示XLSX格式

        # 关闭工作簿
        wb.Close(SaveChanges=False)
    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        # 退出Excel应用程序
        excel.Application.Quit()


for root,dirs,files in os.walk(folder_path):
    for file in files:
        if file.endswith(".xls"):
        # if file == '建（构）筑物.xls':
            xls_file =os.path.join(root,file)
            xlsx_file = xls_file.replace(".xls",".xlsx")
            # print(xls_file)
            # print(xlsx_file)
            xlsToXlsx(xls_file,xlsx_file)
            os.remove(xls_file)

print("\nDone")