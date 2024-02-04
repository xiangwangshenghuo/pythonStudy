from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget(self)
        a = dir(self.list_widget)
        print(a)
        l = []
        for i in a:
            if hasattr(self.list_widget, i):
                continue
            l.append(i)
        print(l)

        self.setCentralWidget(self.list_widget)

        items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 设置文本对齐方式为靠左对齐
            self.list_widget.addItem(item)

        self.list_widget.setViewMode(QListWidget.IconMode)  # 设置列表视图模式为图标模式
        self.list_widget.setResizeMode(QListWidget.Adjust)  # 设置调整大小策略为适应内容

        self.list_widget.setStyleSheet("QListWidget::item { padding: 4px; }")  # 设置item的内边距


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
