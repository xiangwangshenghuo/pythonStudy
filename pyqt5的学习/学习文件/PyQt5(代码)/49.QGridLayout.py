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
        layout = QGridLayout()
        layout.addWidget(label1,1,2)
        # layout.addWidget(label2)
        # layout.addWidget(label3)
        self.setLayout(layout)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())