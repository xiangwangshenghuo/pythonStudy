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
        # 盒子布局:必须传入一个布局方向
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        # 调整外边距：就是距离父控件的四边的距离
        layout.setContentsMargins(20,20,30,30)
        # 设置每个控件间的距离：内边距
        layout.setSpacing(60)

        label4 = QLabel('好好学习4')
        label4.setStyleSheet('background-color:red;')
        label4.adjustSize()
        # 替换布局中的子控件: 必须隐藏，或者删除被置换的控件，不再被此布同管理
        # layout.replaceWidget(label2, label4)
        # label2.setParent(None) # 没有引用，自动释放

        # 布局嵌套
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
        # 添加布局和控件也是分先后关系的
        layout.addLayout(h_layout)
        layout.addWidget(label4)
        # 设置布局能用性
        layout.setEnabled(True)
        # 设置控件的布局  将布局控件内部的子控件添加到布局管理器中，自动进行布局·注意，创建子控件时，不需要设置父控件基类。
        self.setLayout(layout)
        # 设置控件的布局方向 设置给需要布局子控件的父控件\调整方向
        # self.setLayoutDirection(Qt.RightToLeft)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())