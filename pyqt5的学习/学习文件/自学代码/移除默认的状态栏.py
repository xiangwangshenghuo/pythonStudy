from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStatusBar(None)
        self.setMenuBar(None)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
