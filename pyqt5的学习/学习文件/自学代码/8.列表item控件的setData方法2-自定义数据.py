from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

app = QApplication([])

list_widget = QListWidget()

# 创建第一个item，并设置显示文本和类型为0
item1 = QListWidgetItem("Item 1")
item1.setData(Qt.UserRole, 0)  # 设置类型为0
list_widget.addItem(item1)

# 创建第二个item，并设置显示文本和类型为1
item2 = QListWidgetItem("Item 2")
item2.setData(Qt.UserRole, 1)  # 设置类型为1
list_widget.addItem(item2)

# 创建第三个item，并设置显示文本和类型为1
item2 = QListWidgetItem("Item 3")
item2.setData(Qt.UserRole, 1)  # 设置类型为1
list_widget.addItem(item2)

list_widget.show()

app.exec_()
