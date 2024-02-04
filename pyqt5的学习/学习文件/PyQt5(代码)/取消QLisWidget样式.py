from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget

app = QApplication([])

list_widget = QListWidget()
for i in range(100):
    list_widget.addItem('Item' + str(i))

# 取消鼠标移入时的效果
style_sheet = """
    QListWidget::item:hover {
        background: white;
        color:black;
    }
    QListWidget::item:selected {
        background: white;
        color:red;
        border-width:0px
    }
"""

# list_widget.setStyleSheet("""
#     QListWidget::item:selected:active {
#         background-color: 'white';
#         color: none;
#     }
# """)
# list_widget.setMouseTracking(False)

list_widget.setStyleSheet(style_sheet)

# list_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
# list_widget.setStyleSheet(style_sheet)

# 取消选中项的效果
# list_widget.setSelectionMode(QListWidget.NoSelection)
# list_widget.setCurrentItem(None)
# list_widget.setStyleSheet("QListWidget::item:selected{background: white; color: black;border-color:white;}")
# list_widget.setStyleSheet("QListWidget::item:selected { }")

list_widget.show()
app.exec_()
