import threading
import time

def my_thread():
    while True:
        print("子线程正在运行")
        time.sleep(1)

# 创建子线程，并将其设置为守护线程
thread = threading.Thread(target=my_thread)
thread.daemon = True

# 启动子线程
thread.start()

# 主线程继续执行其他操作
time.sleep(5)
print("主线程即将退出")
