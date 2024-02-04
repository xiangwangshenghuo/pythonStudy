from PyQt5.Qt import *

class Btn(QPushButton):
    rightCliked = pyqtSignal()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # print(evt.button())
        if evt.button() == Qt.RightButton:
            print('发射右击信号')
            self.rightCliked.emit()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn = Btn('xx', self)
        # self.btn.pressed.connect(lambda :print('按钮被点击了'))
        btn.rightCliked.connect(lambda :print('按钮被点击了'))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())