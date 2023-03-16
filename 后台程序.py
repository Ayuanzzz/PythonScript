from daemonize import Daemonize

def main_program():
    # 在这里编写你的主要程序逻辑
    pass

if __name__ == '__main__':
    # 定义一个守护进程对象
    daemon = Daemonize(app="huhuApp", pid="/tmp/huhuApp.pid", action=main_program)
    # 启动守护进程
    daemon.start()
