# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       百川一页
-------------------------------------------------
"""
__author__ = 'Sz'

from PyQt5.Qt import *
import sys

# 创建app应用程序
app = QApplication(sys.argv)

window = QWidget()
# 设置标题
window.setWindowTitle("社会我顺哥,人狠话不多")
# 设置窗口大小
window.resize(500, 500)
# 窗口位置
window.move(400, 200)

# 文本组件
label = QLabel(window)
# 文本内容
label.setText("Hello Sz")
# 文本在窗口的位置
label.move(200, 200)

# 显示窗口
window.show()

#
# app.exec_() 执行应用程序，并进入消息循环， 返回退出码
sys.exit(app.exec_())
