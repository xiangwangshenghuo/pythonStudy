import json
import os.path
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
#                              水平布局  垂直布局
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
# 导入按钮
from PyQt5.QtWidgets import QPushButton
# 导入输入框
from PyQt5.QtWidgets import QLineEdit

# 导入表格
from PyQt5.QtWidgets import QTableWidget
# 导入单元格对象,修改表格每列标题信息
from PyQt5.QtWidgets import QTableWidgetItem

# 导入文本显示框
from PyQt5.QtWidgets import QLabel

# 导入qt,用它设置表格单元格不能被修改
from PyQt5.QtCore import Qt



# 读取json
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

#
STATUS_MAPPING = {
    0:"初始化中",
    1:'待执行1',
    3:'待执行3',
    10:'待执行10',
    11:'待执行11',

}

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置窗口名称
        self.setWindowTitle('NB的xx系统')
        # 窗口尺寸
        self.resize(1228, 450)
        # 窗口位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 垂直方向的布局
        layout = QVBoxLayout()

        # 1.创建顶部菜单布局(局部水平布局)
        header_layout = self.init_header()
        layout.addLayout(header_layout)

        # 2. 创建上面标题布局
        form_layout = self.init_form()
        layout.addLayout(form_layout)

        # 3. 创建中间表格布局
        table_layout = self.init_table()
        layout.addLayout(table_layout)

        # 4. 创建底部菜单
        footer_layout = self.init_footer()
        layout.addLayout(footer_layout)

        # 设置窗体的元素排列方式,把布局渲染到窗口上
        self.setLayout(layout)

    def init_header(self):
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
        # 添加弹簧
        header_layout.addStretch()
        return header_layout

    def init_form(self):
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        #
        txt_asin.setPlaceholderText("请输入你的商品id和价格：例如1212113=213")
        form_layout.addWidget(txt_asin)
        # 2.2 添加按钮
        btn_add = QPushButton("添加商品")
        form_layout.addWidget(btn_add)
        return form_layout

    def init_table(self):
        table_layout = QHBoxLayout()

        # 创建2行8列的表格
        table_widget = QTableWidget(0, 8)
        table_header = [
            {'field': "asin", "text": 'ASIN', "width": 120},
            {'field': "title", "text": '标题', "width": 150},
            {'field': "url", "text": 'URL', "width": 400},
            {'field': "price", "text": '低价', "width": 100},
            {'field': "success", "text": '成功次数', "width": 100},
            {'field': "error", "text": '503次数', "width": 100},
            {'field': "status", "text": '状态', "width": 100},
            {'field': "freequency", "text": '频率(N秒/次)', "width": 100},
        ]
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)
            # 设置0索引对应的列的宽度
            table_widget.setColumnWidth(idx, info['width'])

        # 读取数据
        file_path = os.path.join(BASE_DIR,'db','db.json')
        with open(file_path,mode='r',encoding='utf-8') as f:
            data = f.read()
        data_list = json.loads(data) #['BO8123194', 'AMD er', 'http://www.baidu.com', '300.0',166,1,5]

        # 设置表格的默认显示数据
        # 获取当前表格有多少行
        current_row_count = table_widget.rowCount()
        print(current_row_count)
        for row_list in data_list:
            # 给表格中插入一行
            table_widget.insertRow(current_row_count)
            # 写真实数据
            for id, ele in enumerate(row_list) :
                ele = STATUS_MAPPING[ele] if id == 6 else ele
                cell = QTableWidgetItem(str(ele))
                # 设置单元格是否可以被修改
                if id in [0,4,5,6] :
                    # 设置不可以修改
                    print()
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                # 把单元格cell插入到current_row_count行 id列，
                table_widget.setItem(current_row_count, id, cell)
            # cell = QTableWidgetItem("BO8123194")
            # # 把单元格cell插入到current_row_count行 0列，
            # table_widget.setItem(current_row_count,0,cell)
            current_row_count +=1
        table_layout.addWidget(table_widget)
        return table_layout

    def init_footer(self):
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
        return footer_layout



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())