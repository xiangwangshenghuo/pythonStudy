# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        # 窗口是否为最大化
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

# icon = QIcon("xxx.png")
# window.setWindowIcon(icon)
#
# # QIcon
# print(window.windowIcon())
#
# window.setWindowTitle("社会我顺哥,")
# print(window.windowTitle())
#
# window.setWindowOpacity(0.9)
# print(window.windowOpacity())
# 设置窗口默认为无状态
# print(window.windowState() == Qt.WindowNoState)
# 设置窗口最小化
# window.setWindowState(Qt.WindowMinimized)
# 设置窗口最大化
# window.setWindowState(Qt.WindowMaximized)
# 设置窗口全屏，连标题栏都没有了
# window.setWindowState(Qt.WindowFullScreen)


# w2 = QWidget()
# w2.setWindowTitle("w2")


# 2.3 展示控件
window.show()
# 设置窗口最大化，并直接展示
# window.showMaximized()
# 设置窗口全屏，连标题栏都没有了
# window.showFullScreen()
# window.showMinimized()
# 设置窗口为活动窗口，可以和用户交互的
# window.setWindowState(Qt.WindowActive)

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())