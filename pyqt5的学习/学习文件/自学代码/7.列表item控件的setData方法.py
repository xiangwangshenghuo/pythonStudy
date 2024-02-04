
from PyQt5.Qt import *

app = QApplication([])

list_widget = QListWidget()

# 创建第一个列表项，并设置显示文本
item1 = QListWidgetItem("Item 1")
list_widget.addItem(item1)

# 为第一个列表项设置工具提示
item1.setData(Qt.ToolTipRole, "This is item 1")

# 创建第二个列表项，并设置显示文本和字体
item2 = QListWidgetItem("Item 2")
list_widget.addItem(item2)

font = QFont("Arial", 12, QFont.Bold)
item2.setData(Qt.DisplayRole, "Custom Item 2")
item2.setData(Qt.FontRole, font)

# 创建第三个列表项，并设置显示文本的颜色
item3 = QListWidgetItem("Item 3")
list_widget.addItem(item3)

color = QColor(255, 0, 0)
item3.setData(Qt.DisplayRole, "Custom Item 3")
item3.setData(Qt.ForegroundRole, color)

list_widget.show()

app.exec_()
