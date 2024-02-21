import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QListWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ltWds = []
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.btn = QPushButton('Button', self)
        self.btn.clicked.connect(self.clickBtn)

        self.grid.addWidget(self.btn, 0, 0)

    def clickBtn(self):
        # try:
        #     self.grid.itemAtPosition(1, 1).widget().deleteLater() # 删除之前的控件
        # except Exception as e:
        #     print(e)
        #     pass
        if self.grid.count() < 20:
            self.lw = QListWidget()
            self.ltWds.append(self.lw)

            self.lw.addItem("Item "+str(self.grid.count()))
            self.grid.addWidget(self.lw, 1, 1)
        else:
            self.lw.hide()
            self.lw = random.choice(self.ltWds)
            self.lw.show()
            self.grid.addWidget(self.lw,1,1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
