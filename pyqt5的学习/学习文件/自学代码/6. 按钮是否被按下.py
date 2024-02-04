import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print(self.button.isChecked())
        if self.button.isChecked():
            print('Button is clicked')
        else:
            print('Button is NOT clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
