import pyodbc
import os


def addColumn(mdb_path):
    DBQ = f"DBQ={mdb_path};"
    conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + DBQ)
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    # 定义 SQL 语句来向 BOUL 表添加 SHAPE 列
    sql1 = "ALTER TABLE BOUL ADD COLUMN OBJECTID AUTOINCREMENT PRIMARY KEY"
    sql2 = "ALTER TABLE BOUL ADD COLUMN SHAPE OLEOBJECT"
    sql3 = "ALTER TABLE BOUA ADD COLUMN OBJECTID AUTOINCREMENT PRIMARY KEY"
    sql4 = "ALTER TABLE BOUA ADD COLUMN SHAPE OLEOBJECT"
    sql5 = "ALTER TABLE BXZA ADD COLUMN OBJECTID AUTOINCREMENT PRIMARY KEY"
    sql6 = "ALTER TABLE BXZA ADD COLUMN SHAPE OLEOBJECT"
    sql7 = "ALTER TABLE BQTL ADD COLUMN OBJECTID AUTOINCREMENT PRIMARY KEY"
    sql8 = "ALTER TABLE BQTL ADD COLUMN SHAPE OLEOBJECT"
    try:
        # 执行 SQL 语句
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
        cursor.execute(sql6)
        cursor.execute(sql7)
        cursor.execute(sql8)

        conn.commit()
        print(f"修改{mdb_path}成功\n")
    except Exception as e:
        print(f"{mdb_path}: {e}")
    finally:
        # 关闭连接
        cursor.close()
        conn.close()


if __name__ == "__main__":
    folder_path = input('请输入mdb文件夹路径: ')
    mdb_files = [file for file in os.listdir(folder_path) if file.endswith(".mdb") or file.endswith(".MDB")]
    for mdb_file in mdb_files:
        mdb_path = os.path.join(folder_path, mdb_file)
        print(mdb_path)
        addColumn(mdb_path)
    print('\n修改完成')
input('按任意键退出')
