"""
在PyQt5中，QToolBox是一个可折叠的工具箱，可以包含多个可折叠的小部件，使得用户可以在不同的页面之间切换。

使用QToolBox的基本步骤如下：

创建一个QToolBox对象：tool_box = QToolBox()
创建需要添加到QToolBox中的小部件（例如QGroupBox）：group_box1 = QGroupBox("Group 1")
把小部件添加到QToolBox中：tool_box.addItem(group_box1, "Group 1")
重复步骤2和3以添加更多的小部件。
把QToolBox添加到窗口或其他父部件中：layout.addWidget(tool_box)
下面是一个完整的例子，展示了如何使用QToolBox创建一个包含两个折叠小部件的窗口：
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QGroupBox, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QToolBox Example")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 创建QToolBox对象
        tool_box = QToolBox()

        # 创建第一个小部件
        group_box1 = QGroupBox("Group 1")
        label1 = QLabel("Content for Group 1")
        layout1 = QVBoxLayout()
        layout1.addWidget(label1)
        group_box1.setLayout(layout1)

        # 将第一个小部件添加到QToolBox中
        tool_box.addItem(group_box1, "Group 1")

        # 创建第二个小部件
        group_box2 = QGroupBox("Group 2")
        label2 = QLabel("Content for Group 2")
        layout2 = QVBoxLayout()
        layout2.addWidget(label2)
        group_box2.setLayout(layout2)

        # 将第二个小部件添加到QToolBox中
        tool_box.addItem(group_box2, "Group 2")

        # 将QToolBox添加到窗口布局中
        layout.addWidget(tool_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
