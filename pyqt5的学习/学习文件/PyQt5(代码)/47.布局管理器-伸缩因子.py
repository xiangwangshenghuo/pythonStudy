from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('好好学习1')
        label1.setStyleSheet('background-color:cyan;')
        label1.adjustSize()
        label2 = QLabel('好好学习2')
        label2.setStyleSheet('background-color:yellow;')
        label2.adjustSize()
        label3 = QLabel('好好学习3')
        label3.setStyleSheet('background-color:red;')
        label3.adjustSize()
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(label1,1) # 参数stretch伸缩因子：就是在拉伸窗口时多余的空白部分该如何分配 占用1分
        layout.addWidget(label2,2) # 就是把空白部分求出总份数，它占用2分
        # layout.addStretch(2) # 空白占用2份，但是当窗口调小时，它可以变没
        layout.addStretch() # 如果不传参，默认0，空白部分就是占用0分，如果其他的控件没有设置伸缩因子，就是把多余的空白优先给它，
        layout.addWidget(label3,1) # 占用1分
        # 设置伸缩因子：可以给子布局或者子控件
        layout.setStretchFactor(label1,2)

        self.setLayout(layout)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())