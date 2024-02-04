from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("This is a very long text that will be automatically word wrapped.")
label.setWordWrap(True)
label.show()
app.exec_()
