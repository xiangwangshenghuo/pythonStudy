import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.listWidget = QListWidget(self)
        self.listWidget.addItems(["Item 1", "Item 2", "Item 3"])
        self.listWidget.itemSelectionChanged.connect(self.onItemSelected)

        layout.addWidget(self.listWidget)
        self.setLayout(layout)
        self.show()

    def onItemSelected(self):
        selected_items = self.listWidget.selectedItems()
        if selected_items:
            selected_item_text = selected_items[0].text()
            print(f"Selected item: {selected_item_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())