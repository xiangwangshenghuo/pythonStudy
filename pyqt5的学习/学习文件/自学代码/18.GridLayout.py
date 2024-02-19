from PyQt5.Qt import *
#
# app = QApplication([])
# window = QWidget()
# layout = QGridLayout(window)
#
# # 添加一个按钮到网格布局的左上角
# button1 = QPushButton('Button 1')
# layout.addWidget(button1, 0, 0)
#
# # 添加一个按钮到网格布局的右上角，按钮右对齐
# button2 = QPushButton('Button 2')
# layout.addWidget(button2, 0, 1, alignment=Qt.AlignRight)
#
# # 添加一个按钮到网格布局的左下角，按钮占据两行
# button3 = QPushButton('Button 3')
# layout.addWidget(button3, 1, 0, 2, 1)
#
# window.show()
# app.exec_()

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

app = QApplication([])

# 创建QWidget并设置大小
window = QWidget()
window.setFixedSize(280, 400)

# 创建网格布局并添加到QWidget
grid_layout = QGridLayout(window)

# 创建Label并添加到网格布局的0,0位置，占据5行
label1 = QLabel("This is a long label.")
grid_layout.addWidget(label1, 0, 0, 5, 1)

# 创建Label并添加到网格布局的5,0位置
label2 = QLabel("Label 2")
grid_layout.addWidget(label2, 5, 0)

# 创建Label并添加到网格布局的6,0位置
label3 = QLabel("Label 3")
grid_layout.addWidget(label3, 6, 0)
# 添加占位控件
spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
grid_layout.addItem(spacer,7,0)
# 创建按钮，设置大小并添加到网格布局的8,0位置
button = QPushButton('Button')
button.setFixedSize(180, 40)
grid_layout.addWidget(button, 8, 0)

# 显示QWidget
window.show()

# 运行程序
app.exec_()

