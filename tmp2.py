import psutil

# 获取所有进程
for process in psutil.process_iter():
    try:
        # 判断进程是否为要查找的进程
        if process.name() == "LetsPRO.exe":
            # 输出该进程的 PID
            print(process.pid)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
