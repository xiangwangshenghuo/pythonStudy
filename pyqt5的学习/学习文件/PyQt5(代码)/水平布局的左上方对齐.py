# import sys
#
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#         self.setLayout(hbox)
#
#         lbl_big = QLabel('This is a long text for big QLabel')
#         lbl_big.setFixedSize(300, 300)
#         hbox.addWidget(lbl_big, alignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
#
#         lbl_small = QLabel('Short text')
#         lbl_small.setFixedSize(100, 100)
#         hbox.addWidget(lbl_small, alignment = QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
#
#         self.setGeometry(300, 300, 400, 400)
#         self.setWindowTitle('QHBoxLayout Example')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        lbl_big = QLabel('This is a long text for big QLabel')
        lbl_big.setFixedSize(300, 300)

        lbl_small = QLabel('Short text')
        lbl_small.setFixedSize(100, 100)

        hbox.addWidget(lbl_big)
        vbox.addWidget(lbl_small)

        vbox.addStretch()

        hbox.addLayout(vbox)

        hbox.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.setLayout(hbox)
        self.setWindowTitle('QHBoxLayout Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

