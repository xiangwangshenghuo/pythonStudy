from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class WindowPattern(QMainWindow):
    """
    设置窗口样式（主要是窗口边框、标题栏和窗口本身的样式）

    """
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.resize(500, 260)
        self.setWindowTitle('设置窗口的样式')

        # 最顶端 永远在最前面                                                            无边框（无法拖动）
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # Qt.WindowMinimizeButtonHint
        self.setObjectName('MainWindow')    # 先定义
        self.setStyleSheet("#MainWindow{border-image:url(images/5.png);}")    # 再使用 QSS后边会重点讲解

        # self.imageLabel.setFrameShape(QFrame.NoFrame)
        # # self.imageLabel.setFrameShadow(QFrame.NoFrame)
        # 调整图片-图片随着标签大小而变化
        # self.imageLabel.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WindowPattern()
    print(example.__doc__)
    example.show()
    sys.exit(app.exec_())

