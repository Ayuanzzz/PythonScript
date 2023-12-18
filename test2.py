import win32com.client as win32
import os
import threading
import pythoncom

def xlsToXlsx(xls_file, xlsx_file):
    pythoncom.CoInitialize()
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
        pythoncom.CoUninitialize()

def process_batch(batch):
    for xls_file, xlsx_file in batch:
        xlsToXlsx(xls_file, xlsx_file)
        os.remove(xls_file)

folder_path = r"D:\Python\test\tmp"

# 获取文件列表
xls_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".xls"):
            xls_file = os.path.join(root, file)
            xlsx_file = xls_file.replace(".xls", ".xlsx")
            xls_files.append((xls_file, xlsx_file))

# 分割文件列表成多个批次
batch_size = 5  # 调整批次大小以适应性能需求
batches = [xls_files[i:i + batch_size] for i in range(0, len(xls_files), batch_size)]

# 创建一个线程列表
threads = []

for batch in batches:
    thread = threading.Thread(target=process_batch, args=(batch,))
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

print("\nDone")
