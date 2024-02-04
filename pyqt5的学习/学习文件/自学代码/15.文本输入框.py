import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QTextBrowser, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个文本输入框
        self.text_edit = QTextEdit()

        # 创建一个文本浏览器，并设置为只读模式
        self.text_browser = QTextBrowser()
        self.text_browser.setReadOnly(True)

        # 创建一个垂直布局，并将文本输入框和文本浏览器添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.text_browser)

        # 创建一个主窗口小部件，并将布局设置为主窗口的布局
        widget = QWidget()
        widget.setLayout(layout)

        # 设置主窗口的中心部件
        self.setCentralWidget(widget)

        self.setWindowTitle('输入框')
        self.show()

    def keyPressEvent(self, event):
        # 按下回车键时，在文本浏览器中显示输入的文本
        if event.key() == 16777220:
            text = self.text_edit.toPlainText()
            self.text_browser.append(text)
            self.text_edit.clear()
        else:
            super().keyPressEvent(event)

        # 如果有剪贴板中有图片，将图片显示在文本浏览器中
        if event.matches("Ctrl+V"):
            clipboard = QApplication.clipboard()
            image = clipboard.image()
            if not image.isNull():
                self.text_browser.append('<img src="clipboard:image/png"/>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
