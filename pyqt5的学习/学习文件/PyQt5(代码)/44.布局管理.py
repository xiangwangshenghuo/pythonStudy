from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('好好学习，天天向上1')
        label1.setStyleSheet('background-color:cyan;')
        label1.adjustSize()
        label2 = QLabel('好好学习，天天向上2')
        label2.setStyleSheet('background-color:yellow;')
        label2.adjustSize()
        label3 = QLabel('好好学习，天天向上3')
        label3.setStyleSheet('background-color:red;')
        label3.adjustSize()
        # 垂直布局 子控件的宽度 = 父控件的宽度； 子控件的高度 = 父控件的高度 / 3
        v_layout = QHBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)
        # 调整外边距
        v_layout.setContentsMargins(20,20,30,30)
        # 设置每个控件间的距离
        v_layout.setSpacing(60)
        # 设置控件的布局  将布局控件内部的子控件添加到布局管理器中，自动进行布局·注意，创建子控件时，不需要设置父控件基类。
        self.setLayout(v_layout)
        # 设置控件的布局方向 设置给需要布局子控件的父控件\调整方向
        self.setLayoutDirection(Qt.RightToLeft)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())

# from PyQt5.Qt import *
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("布局管理的学习")
#         self.resize(500, 500)
#         self.setup_ui()
#
#     def setup_ui(self):
#         label1 = QLabel('好好学习1')
#         label1.setStyleSheet('background-color:cyan;')
#         label1.adjustSize()
#         label2 = QLabel('好好学习2')
#         label2.setStyleSheet('background-color:yellow;')
#         label2.adjustSize()
#         label3 = QLabel('好好学习3')
#         label3.setStyleSheet('background-color:red;')
#         label3.adjustSize()
#         layout = QBoxLayout(QBoxLayout.LeftToRight)
#         layout.addWidget(label1)
#         layout.addWidget(label2)
#         layout.addWidget(label3)
#         self.setLayout(layout)
#
#
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#
#     window = Window()
#     window.show()
#
#
#     sys.exit(app.exec_())