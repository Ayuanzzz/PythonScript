import ctypes
import psutil
import time

# 获取所有进程
for process in psutil.process_iter():

    # print(process.name())
    try:
        # 判断进程是否为要查找的进程
        if process.name() == "LetsPRO.exe":
            # 输出该进程的 PID
            print(process.pid)
            pid = process.pid
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# 加载 kernel32.dll 库
kernel32 = ctypes.WinDLL('kernel32')

# 打开进程句柄
PROCESS_TERMINATE = 0x0001
handle = kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)

# 终止进程
kernel32.TerminateProcess(handle, -1)

time.sleep(3)

ctypes.windll.shell32.ShellExecuteW(None, "runas", "C:\Program Files (x86)\letsvpn\LetsPRO.exe", None, None, 0x20000)
