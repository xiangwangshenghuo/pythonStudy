import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDesktopWidget
#                              水平布局  垂直布局
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
# 导入按钮
from PyQt5.QtWidgets import QPushButton
# 导入输入框
from PyQt5.QtWidgets import QLineEdit

# 导入表格
from PyQt5.QtWidgets import QTableWidget
# 导入修改表格每列标题信息
from PyQt5.QtWidgets import QTableWidgetItem

# 导入文本显示框
from PyQt5.QtWidgets import QLabel


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口名称
        self.setWindowTitle('NB的xx系统')
        # 窗口尺寸
        self.resize(1228,450)
        #窗口位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 垂直方向的布局
        layout = QVBoxLayout()

        # 1. 创建顶部菜单布局(局部水平布局)
        header_layout = QHBoxLayout()

        # 1.1 创建两个按钮
        btn_start = QPushButton('开始')
        # 给按钮设置高度
        # btn_start.setFixedSize(100)
        header_layout.addWidget(btn_start)
        btn_stop = QPushButton('停止')
        # addWidget添加插件
        header_layout.addWidget(btn_stop)
        # addLayout添加布局
        layout.addLayout(header_layout)
        # 添加弹簧
        header_layout.addStretch()

        # 2. 创建上面标题布局
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        #
        txt_asin.setPlaceholderText("请输入你的商品id和价格：例如1212113=213")
        form_layout.addWidget(txt_asin)
        # 2.2 添加按钮
        btn_add = QPushButton("添加商品")
        form_layout.addWidget(btn_add)
        layout.addLayout(form_layout)

        # 3. 创建中间表格布局
        table_layout = QHBoxLayout()

        # 3.1
        # 创建2行8列的表格
        table_widget = QTableWidget(1,8)
        table_header = [
            {'field':"asin","text":'ASIN',"width":120},
            {'field':"title","text":'标题',"width":150},
            {'field':"url","text":'URL',"width":400},
            {'field':"price","text":'低价',"width":100},
            {'field':"success","text":'成功次数',"width":100},
            {'field':"error","text":'503次数',"width":100},
            {'field':"status","text":'状态',"width":100},
            {'field':"freequency","text":'频率(N秒/次)',"width":100},
        ]
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)
            # 设置0索引对应的列的宽度
            table_widget.setColumnWidth(idx, info['width'])

        # 通过上述方法可以循环设置表头和宽度
        # # 设置表格的索引为0的元素文本信息，需要导入QTableWidgetItem
        # item = QTableWidgetItem()
        # item.setText('标题')
        # table_widget.setHorizontalHeaderItem(0,item)
        # # 设置0索引对应的列的宽度
        # table_widget.setColumnWidth(0,120)
        #
        # item = QTableWidgetItem()
        # item.setText('网址')
        # table_widget.setHorizontalHeaderItem(1, item)
        # # 设置1索引对应的列的宽度
        # table_widget.setColumnWidth(1, 400)

        table_layout.addWidget(table_widget)
        layout.addLayout(table_layout)

        # 4. 创建底部菜单
        footer_layout = QHBoxLayout()

        label_status = QLabel('未检测')
        footer_layout.addWidget(label_status)
        footer_layout.addStretch()
        btn_reinit = QPushButton('重新初始化')
        footer_layout.addWidget(btn_reinit)
        btn_recheck = QPushButton('重新检测')
        footer_layout.addWidget(btn_recheck)
        btn_reset = QPushButton('次数清零')
        footer_layout.addWidget(btn_reset)
        btn_delete = QPushButton('删除检测项')
        footer_layout.addWidget(btn_delete)
        btn_alert = QPushButton('SMTP报警配置')
        footer_layout.addWidget(btn_alert)
        btn_proxy = QPushButton('代理IP')
        footer_layout.addWidget(btn_proxy)



        layout.addLayout(footer_layout)


        # 垂直布局弹簧
        # layout.addStretch()
        # 设置窗体的元素排列方式,把布局渲染到窗口上
        self.setLayout(layout)

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())