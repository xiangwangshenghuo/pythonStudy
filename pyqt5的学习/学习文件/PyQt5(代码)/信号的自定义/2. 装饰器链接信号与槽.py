from PyQt5.Qt import *




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('xx', self)
        btn.setObjectName('btn')
        btn.move(100,100)

        btn2 = QPushButton('xx', self)
        btn2.setObjectName('btn')
        btn2.move(300, 100)

        QMetaObject.connectSlotsByName(self)


    @pyqtSlot(bool)
    def on_btn_clicked(self, val):
        # 名称必须是这样写
        print('按钮被点击',val)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())