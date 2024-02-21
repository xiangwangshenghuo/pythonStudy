from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon

app = QApplication([])
list_widget = QListWidget()

item = QListWidgetItem()
item.setIcon(QIcon('0.jpg'))  # 将 'boy.png' 替换为你的图像路径
item.setText("这是第一行\n这是第二行")

list_widget.addItem(item)
list_widget.show()

app.exec_()

