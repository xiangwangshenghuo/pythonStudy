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
        # 1.创建布局管理器对象:必须传入一个布局方向
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        # 2. 把布局管理器对象设置为需要布局的父控件
        # 注意，创建子控件时，不需要设置父控件基类。
        self.setLayout(layout)
        # 3. 添加需要布局的子控件到布局管理器中
        layout.addWidget(label1)
        layout.addWidget(label2)
        # 在子控件1,2之间添加空白布局
        layout.addSpacing(100)
        layout.addWidget(label3)

        # 插入空白:索引值不包括空白的
        layout.insertSpacing(3,100)

        # 插入控件
        label4 = QLabel('好好学习4')
        label4.setStyleSheet('background-color:red;')
        label4.adjustSize()
        layout.insertWidget(1, label4)
        # 插入布局
        label5 = QLabel('好好学习5')
        label5.setStyleSheet('background-color:blue;')
        label6 = QLabel('好好学习6')
        label6.setStyleSheet('background-color:green;')
        label7 = QLabel('好好学习7')
        label7.setStyleSheet('background-color:pink;')
        h_layout = QBoxLayout(QBoxLayout.TopToBottom)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)
        layout.insertLayout(2,h_layout)

        # 从布局中移出控件，但是还是在父控件上,所以需要删除或者隐藏
        # layout.removeWidget(label1)
        # label1.hide()


        # timer = QTimer(self)
        #
        # def test():
        #     layout.setDirection((layout.direction() + 1) % 4)
        #     pass
        #
        # timer.timeout.connect(test)
        # timer.start(1000)

        # 设置控件的布局  将布局控件内部的子控件添加到布局管理器中，自动进行布局·注意，创建子控件时，不需要设置父控件基类。
        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())