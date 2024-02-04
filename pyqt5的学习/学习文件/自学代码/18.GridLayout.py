from PyQt5.Qt import *

app = QApplication([])
window = QWidget()
layout = QGridLayout(window)

# 添加一个按钮到网格布局的左上角
button1 = QPushButton('Button 1')
layout.addWidget(button1, 0, 0)

# 添加一个按钮到网格布局的右上角，按钮右对齐
button2 = QPushButton('Button 2')
layout.addWidget(button2, 0, 1, alignment=Qt.AlignRight)

# 添加一个按钮到网格布局的左下角，按钮占据两行
button3 = QPushButton('Button 3')
layout.addWidget(button3, 1, 0, 2, 1)

window.show()
app.exec_()
