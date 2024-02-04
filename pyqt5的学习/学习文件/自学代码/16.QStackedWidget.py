import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton,QLabel

class StackedWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QStackedWidget Example')

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(QLabel('聊天'))  # 第一页
        self.stacked_widget.addWidget(QLabel('通讯录'))  # 第二页

        button1 = QPushButton('显示第一页')
        button1.clicked.connect(self.showPage1)

        button2 = QPushButton('显示第二页')
        button2.clicked.connect(self.showPage2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stacked_widget)
        vbox.addWidget(button1)
        vbox.addWidget(button2)

        self.setLayout(vbox)

    def showPage1(self):
        self.stacked_widget.setCurrentIndex(0)  # 显示第一页

    def showPage2(self):
        self.stacked_widget.setCurrentIndex(1)  # 显示第二页

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StackedWidgetExample()
    ex.show()
    sys.exit(app.exec_())
