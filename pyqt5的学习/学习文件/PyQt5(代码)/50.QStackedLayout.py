from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 1. 创建布局管理器对象
        sl = QStackedLayout()
        # 2. 把布局对象设置为需要布局布的父控件,必须放到前边
        self.setLayout(sl)
        # 3. 通过布局对象，布局子控件
        label1 = QLabel('好好学习1')
        label1.setStyleSheet('background-color:cyan;')
        label1.adjustSize()
        label2 = QLabel('好好学习2')
        label2.setStyleSheet('background-color:yellow;')
        label2.adjustSize()
        label3 = QLabel('好好学习3')
        label3.setStyleSheet('background-color:red;')
        label3.adjustSize()
        label4 = QLabel('好好学习4')
        label4.setStyleSheet('background-color:red;')
        label4.adjustSize()

        label5 = QLabel('好好学习5')
        label5.setStyleSheet('background-color:blue;')
        label6 = QLabel('好好学习6')
        label6.setStyleSheet('background-color:green;')
        label7 = QLabel('好好学习7')
        label7.setStyleSheet('background-color:pink;')
        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)
        # 一、添加控件
        print(sl.addWidget(label1))
        sl.addWidget(label2)
        sl.addWidget(label3)
        # 二、插入控件
        print(sl.currentIndex())
        sl.insertWidget(0, label4)
        print(sl.currentIndex())
        # 三、获取控件
        print(sl.widget(1).text())
        # 四、指明显示哪个空间,切换
        sl.setCurrentIndex(2)
        timer = QTimer(self)
        timer.timeout.connect(lambda : sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
        timer.start(1000)
        # 五。信号 传入索引
        sl.currentChanged.connect(lambda val: print(val))
        sl.widgetRemoved.connect(lambda val: print(val))
        # 六、展示 StackAll StackAOne
        sl.setStackingMode(QStackedLayout.StackAll)







if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())