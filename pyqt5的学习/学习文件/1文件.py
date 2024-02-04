from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# import time, datetime
app = QApplication(sys.argv)  # 创建应用程序
MainWindow= QWidget()  # 创建窗口
# MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")  # 设置窗口的对象名称
MainWindow.setWindowTitle("ERP系统欢迎您")  # 设置窗口标题
MainWindow.resize(800, 600)  # 设置窗口尺寸大小
MainWindow.move(500, 100)  # 设置窗口位置
MainWindow.setWindowOpacity(1.0)  # 设置窗口透明度

icon = QtGui.QIcon()  # 定义图标
icon.addPixmap(QtGui.QPixmap("image/未标题-5.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 指定窗口图标路径
MainWindow.setWindowIcon(icon)  # 设置图片为主窗口的图标
MainWindow.setWindowFlags(QtCore.Qt.Widget)  # 默认窗口，显示最大化、最小化、关闭按钮
# 新建菜单栏
menubar = QtWidgets.QMenuBar(MainWindow)
menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))  # 分别是输入框的横向位置（数字越大越往右）、输入框的纵向位置（数字越大越往下）、输入框的长度、输入框的宽度
menubar.setObjectName("menubar")
#  根菜单1_____________________________________________________________________________________________________
menu_1 = menubar.addMenu('控制台')
menu_1.setObjectName('menu_1')
# 二级菜单1_1___________________________________________________________________
menu_1_1 = QtWidgets.QAction(menu_1)
menu_1.addAction('用户登录')
menu_1_1.setObjectName('menu_1_1')

# 设置菜单快捷方式？
menu_1_1.setShortcut('Ctrl+N')

# 设置菜单图标？
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap('image/未标题-5.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
menu_1_1.setIcon(icon)

# 设置状态栏？
Statusbar = QtWidgets.QStatusBar(MainWindow)
Statusbar.setObjectName("Statusbar")
Statusbar.showMessage('Status bar messages，3000')  # 状态栏显示'Status bar messages，显示此消息3000ms

MainWindow.show()
sys.exit(app.exec_())

