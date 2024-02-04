import sys
import threading
import time

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Communication(QObject):
    message_received = pyqtSignal(str)

class MainWindow(QMainWindow):
    message_received = pyqtSignal(str)
    def __init__(self):
        super(MainWindow, self).__init__()

        self.label = QLabel(self)
        self.label.move(50, 50)

    def update_label(self, message):
        self.label.setText(message)

class ServerThread(threading.Thread):
    def __init__(self, communication):
        super(ServerThread, self).__init__()
        self.communication = communication

    def run(self):
        # 在这个示例中，使用一个简单的循环来模拟从服务器接收数据
        i = 0
        while True:
            time.sleep(3)
            # 假设从服务器接收到的数据是 "Hello, World!"
            message = "Hello, World!" + str(i)
            # self.communication.message_received.emit(message)
            window.message_received.emit(message)
            i += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # 创建一个用于通信的对象
    communication = Communication()

    # 创建一个子线程，并将通信对象传递给它
    server_thread = ServerThread(communication)
    server_thread.start()

    # 将信号与窗口上的更新函数连接起来
    window.message_received.connect(window.update_label)

    window.show()
    sys.exit(app.exec_())
