import pyodbc
import os
import shutil

# folder_path = r"D:\Python\data\test3"
folder_path = input("Folder: ")

file_names = os.listdir(folder_path)
mdb_paths = [os.path.join(folder_path, file) for file in file_names if file.endswith(".mdb")]

def createDir(num):
    dir_path = os.path.join(folder_path,num)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

def moveFile(num,basename,mdb,dwg):
    new_folder = os.path.join(folder_path, num)
    mdb_new = os.path.join(new_folder, basename)
    dwg_new = mdb_new.replace(".mdb", ".dwg")
    try:
        shutil.copy(mdb, mdb_new)
        shutil.copy(dwg, dwg_new)
    except Exception as e:
        # 处理其他异常的代码
        print(f"发生了异常：{e}")

def rdAccess(path):
    print(path)
    global rows
    DBQ = f"DBQ={path};"
    conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + DBQ)
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    table_name = "GDB_SpatialRefs"
    crsr.execute(f"SELECT * FROM {table_name}")
    # 获取所有行
    rows = crsr.fetchall()

    dwg_old=path.replace(".mdb",".dwg")
    basename=os.path.basename(path)
    # 遍历行并处理数据
    for row in rows:
        column2_value = row[1]
        if "99E" in column2_value:
            createDir("99")
            moveFile("99",basename,path,dwg_old)
        elif "96E" in column2_value:
            createDir("96")
            moveFile("96", basename, path, dwg_old)
        elif "93E" in column2_value:
            createDir("93")
            moveFile("93", basename, path, dwg_old)

for mdb_path in mdb_paths:
    rdAccess(mdb_path)

print("\nDone")

input("\nnexit")