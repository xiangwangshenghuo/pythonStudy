from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea, \
    QLineEdit, QScrollBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.num = 1
        # 创建垂直布局
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(10)  # 设置垂直布局中各个控件之间的间距



        # 创建滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # 设置滚动区域的大小可变
        self.scroll_area.setHorizontalScrollBarPolicy(1)  # 设置滚动区域只有水平滚动条
        self.scroll_area.setVerticalScrollBarPolicy(1)  # 设置滚动区域只有垂直滚动条

        # 将垂直布局设置为滚动区域的窗口部件，并设置滚动区域为主窗口的布局
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.vertical_layout)
        self.scroll_area.setWidget(self.scrollWidget)

        # 创建发送按钮，并放在主窗口的右下角
        self.send_button = QPushButton('发送')
        self.send_button.clicked.connect(self.add_horizontal_layout)  # 点击按钮时触发添加水平布局的函数
        self.send_button.setFixedSize(80, 30)  # 设置按钮的固定大小

        # 设置主窗口的布局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        main_layout.addStretch()
        main_layout.addWidget(self.send_button)
        # 创建初始的水平布局，并添加到垂直布局
        self.add_horizontal_layout()
        self.setLayout(main_layout)

    def add_horizontal_layout(self):
        # 创建水平布局
        horizontal_layout = QHBoxLayout()

        # 添加控件到水平布局
        label = QLabel('Label' + str(self.num))
        self.num += 1
        edit = QLineEdit()
        horizontal_layout.addWidget(label)
        horizontal_layout.addWidget(edit)

        # 添加水平布局到垂直布局
        self.vertical_layout.insertLayout(self.vertical_layout.count(), horizontal_layout)  # 放在倒数第二个位置，即占位控件之前

        # 滚动至最下方
        bar = self.scroll_area.verticalScrollBar()
        bar.setValue(bar.maximum())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
