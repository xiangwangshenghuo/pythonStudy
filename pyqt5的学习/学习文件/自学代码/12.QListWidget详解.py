# 1. addItem(item): 向列表中添加一个QListWidgetItem对象。
#
# 例子：
#
# ```python
# list_widget = QListWidget()
# item = QListWidgetItem('Item 1')
# list_widget.addItem(item)
# ```
#
# 2. addItem(label): 向列表中添加一个带有给定标签的QListWidgetItem对象。
#
# 例子：
#
# ```python
# list_widget = QListWidget()
# list_widget.addItem('Item 1')
# ```
#
# 3. addItems(labels): 向列表中添加多个带有给定标签的QListWidgetItem对象。
#
# 例子：
#
# ```python
# list_widget = QListWidget()
# list_widget.addItems(['Item 1', 'Item 2', 'Item 3'])
# ```
#
# 4. closePersistentEditor(item): 关闭指定项的持久编辑器。
#
# 例子：
#
# ```python
# list_widget.closePersistentEditor(item)
# ```
#
# 5. count(): 返回列表中项的数量。
#
# 例子：
#
# ```python
# count = list_widget.count()
# ```
#
# 6. currentItem(): 返回当前选中的项。
#
# 例子：
#
# ```python
# item = list_widget.currentItem()
# ```
#
# 7. currentRow(): 返回当前选中项的行号。
#
# 例子：
#
# ```python
# row = list_widget.currentRow()
# ```
#
# 8. editItem(item): 编辑指定项。
#
# 例子：
#
# ```python
# list_widget.editItem(item)
# ```
#
# 9. findItems(text, flags): 根据给定的文本和标志返回匹配的项。
#
# 例子：
#
# ```python
# items = list_widget.findItems('Item', QtCore.Qt.MatchContains)
# ```
#
# 10. indexFromItem(item): 返回给定项的索引。
#
# 例子：
#
# ```python
# index = list_widget.indexFromItem(item)
# ```
#
# 11. insertItem(row, item): 在指定行插入一个项。
#
# 例子：
#
# ```python
# item = QListWidgetItem('New Item')
# list_widget.insertItem(row, item)
# ```
#
# 12. insertItem(row, label): 在指定行插入一个带有给定标签的项。
#
# 例子：
#
# ```python
# list_widget.insertItem(row, 'New Item')
# ```
#
# 13. insertItems(row, labels): 在指定行插入多个带有给定标签的项。
#
# 例子：
#
# ```python
# list_widget.insertItems(row, ['Item 1', 'Item 2', 'Item 3'])
# ```
#
# 14. isItemHidden(item): 检查指定项是否隐藏。
#
# 例子：
#
# ```python
# hidden = list_widget.isItemHidden(item)
# ```
#
# 15. isItemSelected(item): 检查指定项是否被选中。
#
# 例子：
#
# ```python
# selected = list_widget.isItemSelected(item)
# ```
#
# 16. isPersistentEditorOpen(item): 检查指定项的持久编辑器是否打开。
#
# 例子：
#
# ```python
# open = list_widget.isPersistentEditorOpen(item)
# ```
#
# 17. isSortingEnabled(): 检查列表是否启用排序。
#
# 例子：
#
# ```python
# enabled = list_widget.isSortingEnabled()
# ```
#
# 18. item(row): 返回指定行的项。
#
# 例子：
#
# ```python
# item = list_widget.item(row)
# ```
#
# 19. itemAt(p): 返回位于给定坐标点p的项。
#
# 例子：
#
# ```python
# position = QPoint(100, 100)
# item = list_widget.itemAt(position)
# ```
#
# 20. itemAt(x, y): 返回位于给定坐标(x, y)的项。
#
# 例子：
#
# ```python
# item = list_widget.itemAt(100, 100)
# ```
#
# 21. itemFromIndex(index): 返回给定索引的项。
#
# 例子：
#
# ```python
# item = list_widget.itemFromIndex(index)
# ```
#
# 22. itemWidget(item): 返回指定项的关联窗口部件。
#
# 例子：
#
# ```python
# widget = list_widget.itemWidget(item)
# ```
#
# 23. items(data): 返回匹配给定数据的项的列表。
#
# 例子：
#
# ```python
# items = list_widget.items(QtCore.Qt.DisplayRole, 'Item')
# ```
#
# 24. openPersistentEditor(item): 打开指定项的持久编辑器。
#
# 例子：
#
# ```python
# list_widget.openPersistentEditor(item)
# ```
#
# 25. removeItemWidget(item): 移除指定项的关联窗口部件。
#
# 例子：
#
# ```python
# list_widget.removeItemWidget(item)
# ```
#
# 26. row(item): 返回指定项的行号。
#
# 例子：
#
# ```python
# row = list_widget.row(item)
# ```
#
# 27. selectedItems(): 返回选中的项的列表。
#
# 例子：
#
# ```python
# selected_items = list_widget.selectedItems()
# ```
#
# 28. setCurrentItem(item): 设置当前选中的项。
#
# 例子：
#
# ```python
# list_widget.setCurrentItem(item)
# ```
#
# 29. setCurrentItem(item, command): 设置当前选中的项，并指定操作命令。
#
# 例子：
#
# ```python
# list_widget.setCurrentItem(item, QtWidgets.QItemSelectionModel.Select)
# ```
#
# 30. setCurrentRow(row): 设置当前选中的行。
#
# 例子：
#
# ```python
# list_widget.setCurrentRow(row)
# ```
#
# 31. setCurrentRow(row, command): 设置当前选中的行，并指定操作命令。
#
# 例子：
#
# ```python
# list_widget.setCurrentRow(row, QtWidgets.QItemSelectionModel.Select)
# ```
#
# 32. setItemHidden(item, hide): 设置指定项的隐藏状态。
#
# 例子：
#
# ```python
# list_widget.setItemHidden(item, True)
# ```
#
# 33. setItemSelected(item, select): 设置指定项的选中状态。
#
# 例子：
#
# ```python
# list_widget.setItemSelected(item, True)
# ```
#
# 34. setItemWidget(item, widget): 设置指定项的关联窗口部件。
#
# 例子：
#
# ```python
# widget = QWidget()
# list_widget.setItemWidget(item, widget)
# ```
#
# 35. setSortingEnabled(enable): 启用或禁用列表的排序。
#
# 例子：
#
# ```python
# list_widget.setSortingEnabled(True)
# ```
#
# 36. sortItems([order=Qt.AscendingOrder]): 对列表中的项进行排序。可选参数指定排序顺序，默认为升序。
#
# 例子：
#
# ```python
# list_widget.sortItems(QtCore.Qt.DescendingOrder)
# ```
#
# 37. takeItem(row): 移除并返回指定行的项。
#
# 例子：
#
# ```python
# item = list_widget.takeItem(row)
# ```
#
# 38. visualItemRect(item): 返回指定项的可见区域。
#
# 例子：
#
# ```python
# rect = list_widget.visualItemRect(item)
# ```