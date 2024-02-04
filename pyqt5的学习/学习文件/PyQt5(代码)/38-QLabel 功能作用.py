from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel('好好学习，天天向上',self)
        label.setStyleSheet('background-color:cyan;')
        label.move(100,100)
        label.resize(150,300)
        #
        label.adjustSize()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())