from PyQt5.QtWidgets import QApplication, QListWidget

app = QApplication([])
list_widget = QListWidget()
list_widget.addItems(["Item 1", "Item 2", "Item 3"])

# 获取当前选中项的索引
index = list_widget.currentRow()
print(f"当前选中项的索引：{index}")  # 输出：当前选中项的索引：-1，表示没有选中项
index = list_widget.currentIndex()
print(index)

list_widget.setCurrentRow(1)  # 设置选中第2项

index = list_widget.currentRow()
print(f"当前选中项的索引：{index}")  # 输出：当前选中项的索引：1

app.exec_()
