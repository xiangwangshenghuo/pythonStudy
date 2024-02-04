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

# 导入提示框
from PyQt5.QtWidgets import QMessageBox
# 导入菜单框
from PyQt5.QtWidgets import QMenu


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

        # 获取输入框对象
        self.txt_asin = None
        # 表格对象
        self.table_widget = None
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
        btn_start.clicked.connect(self.event_start_click)
        # 给按钮设置高度
        # btn_start.setFixedSize(100)
        header_layout.addWidget(btn_start)
        btn_stop = QPushButton('停止')
        # addWidget添加插件
        header_layout.addWidget(btn_stop)
        # 添加弹簧
        header_layout.addStretch()
        return header_layout

    def event_start_click(self):
        pass

    def init_form(self):
        form_layout = QHBoxLayout()

        # 2.1 输入框
        txt_asin = QLineEdit()
        #
        txt_asin.setText('1=1')# 设置默认输入的值
        # 设置默认背景显示的信息
        # txt_asin.setPlaceholderText("请输入你的商品id和价格：例如1212113=213")
        form_layout.addWidget(txt_asin)
        self.txt_asin = txt_asin
        # 2.2 添加按钮
        btn_add = QPushButton("添加商品")
        # 绑定点击事件
        btn_add.clicked.connect(self.event_add_click)
        form_layout.addWidget(btn_add)
        return form_layout

    def init_table(self):
        table_layout = QHBoxLayout()

        # 创建2行8列的表格
        table_widget = QTableWidget(0, 8)
        self.table_widget = table_widget
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
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                # 把单元格cell插入到current_row_count行 id列，
                table_widget.setItem(current_row_count, id, cell)
            # cell = QTableWidgetItem("BO8123194")
            # # 把单元格cell插入到current_row_count行 0列，
            # table_widget.setItem(current_row_count,0,cell)
            current_row_count +=1

        # 开启右键设置
        table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 右键会触发函数self.right_menu
        table_widget.customContextMenuRequested.connect(self.table_right_menu)


        table_layout.addWidget(table_widget)
        return table_layout

    def table_right_menu(self,pos):
        """

        :param pos: 菜单显示的位置，默认自动传入，不需要手动传入
        :return:
        """
        selected_item_list = self.table_widget.selectedItems()
        if len(selected_item_list) == 0:
            return


        menu = QMenu()
        item_copy = menu.addAction('复制')
        item_log = menu.addAction('查看日志')
        item_log_clear = menu.addAction('清除日志')

        # 选中上述定义哪个的选项
        action = menu.exec_(self.table_widget.mapToGlobal(pos))
        if action == item_copy:
            # 复制当前表格的内容
            # 创建粘贴板对象
            clipboard = QApplication.clipboard()
            # 把选中的内容放到粘贴板里面
            clipboard.setText(selected_item_list[0].text())
        if action == item_log:
            # 查看日志，在对话框展示日志信息
            from utils.dialog import LogDialog
            dialog = LogDialog()
        #     1.模态 ：不能操作窗体以外的界面
        #
        #     非模态：可以操作窗体以外的界面
        #
        # Qt::NonModal // 无模态
        # Qt::WindowModal // 对所有的上级窗口， 模态
        # Qt::ApplicationModal // 对整个应用程序，  模态，阻止一切窗口输入
        # 2.
        # 透明度参数(qreal
        # level)
        #
        # 1.0 = 完全不透明
        #
        # 0.0 = 完全透明 （全0全透）
        # ————————————————
        # 版权声明：本文为CSDN博主「伍铭」的原创文章，遵循CC
        # 4.0
        # BY - SA版权协议，转载请附上原文出处链接及本声明。
        #     dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def init_footer(self):
        footer_layout = QHBoxLayout()

        label_status = QLabel('未检测')
        # 如果后续想要更改显示的内容
        # label_status.setText('检测中')
        # # 改变值后需要使用repaint()刷新
        # label_status.repaint()
        footer_layout.addWidget(label_status)
        footer_layout.addStretch()
        btn_reset = QPushButton('重新初始化')
        btn_reset.clicked.connect(self.event_reset_click)
        footer_layout.addWidget(btn_reset)
        btn_recheck = QPushButton('重新检测')
        footer_layout.addWidget(btn_recheck)
        btn_reset = QPushButton('次数清零')
        footer_layout.addWidget(btn_reset)
        btn_delete = QPushButton('删除检测项')
        btn_delete.clicked.connect(self.event_delete_click)
        footer_layout.addWidget(btn_delete)
        btn_alert = QPushButton('SMTP报警配置')
        btn_alert.clicked.connect(self.event_alert_click)
        footer_layout.addWidget(btn_alert)
        btn_proxy = QPushButton('代理IP')
        btn_proxy.clicked.connect(self.event_proxy_click)
        footer_layout.addWidget(btn_proxy)
        return footer_layout

    # 点击添加按钮
    def event_add_click(self):
        #1. 获取输入框中的内容
        text = self.txt_asin.text()
        text = text.strip()
        if not text:
            QMessageBox.warning(self,'错误','商品ASIN输入错误')
            return
        asin,price = text.split('=')
        price = float(price)
        #2. 加入到表格中（型号和低价
        new_row_list = [asin,"","",price,0,0,0,5]
        current_row_count = self.table_widget.rowCount()

        # 给表格中插入一行
        self.table_widget.insertRow(current_row_count)
        # 写真实数据
        for id, ele in enumerate(new_row_list):
            ele = STATUS_MAPPING[ele] if id == 6 else ele
            cell = QTableWidgetItem(str(ele))
            # 设置单元格是否可以被修改
            if id in [0, 4, 5, 6]:
                # 设置不可以修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(current_row_count,id,cell)
        #3. 发送请求自动获取标题
        # 注意：不能在主线程做爬虫的事，创建一个线程去做爬虫，然后爬到数据，在更新到窗体应用（信号、）
        # 导入定义线程
        from utils.threads import NewTaskThread
        # # 创建线程，传入窗口对象self
        # 注意如果想要传入其他参数，其他参数一定在self前面，
        thread = NewTaskThread(current_row_count, asin, self)
        # # 调用定义线程的信号，连接回调函数，并获取线程传回的数据
        thread.success.connect(self.init_task_success_callback)
        thread.error.connect(self.init_task_error_callback)
        # 开始线程
        thread.start()

    def init_task_success_callback(self,row_index,asin,title,url):
        print(row_index,asin,title,url)
        # 更新标题列
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index,1,cell_title)
        # 更新url列
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)
        # 更新状态列
        cell_status = QTableWidgetItem(STATUS_MAPPING[1])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)

        # 输入框清空
        self.txt_asin.clear()

        pass

    def init_task_error_callback(self, row_index, asin, title, url):
        # 更新标题列
        cell_title = QTableWidgetItem(title)
        self.table_widget.setItem(row_index, 1, cell_title)
        # 更新状态列
        cell_status = QTableWidgetItem(STATUS_MAPPING[11])
        cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.table_widget.setItem(row_index, 6, cell_status)
        # 更新url列
        cell_url = QTableWidgetItem(url)
        self.table_widget.setItem(row_index, 2, cell_url)

        pass

    def event_reset_click(self):
        # 获取已经选中的行，返回列表
        row_list = self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self,'错误', '请选择要重新初始化的行')
            return
        # 获取每一行进行重新初始化
        for row_object in row_list:
            index = row_object.row()
            print('选中第{}行'.format(index))
            # 获取型号
            asin = self.table_widget.item(index,0).text().strip()
            # 状态重新初始化
            cell_status = QTableWidgetItem(STATUS_MAPPING[0])
            cell_status.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.setItem(index,6,cell_status)
            # 创建线程去进行初始化
            from utils.threads import NewTaskThread
            # 注意如果想要传入其他参数，其他参数一定在self前面，
            thread = NewTaskThread(index, asin, self)
            # # 调用定义线程的信号，连接回调函数，并获取线程传回的数据
            thread.success.connect(self.init_task_success_callback)
            thread.error.connect(self.init_task_error_callback)
            # 开始线程
            thread.start()

    def event_delete_click(self):
        row_list = self.table_widget.selectionModel().selectedRows()
        if not row_list:
            QMessageBox.warning(self, '错误', '请选择要重新初始化的行')
            return
        row_list.reverse()
        # 获取每一行进行删除
        for row_object in row_list:
            index = row_object.row()
            # 删除列表中的行
            self.table_widget.removeRow(index)

    # 点击邮件配置
    # 创建一个弹窗，需要单独创建一个文件dialog
    def event_alert_click(self):
        try:
            from utils.dialog import AlertDialog
            dialog = AlertDialog()
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()
        except Exception as e:
            print(e)
        pass

    def event_proxy_click(self):
        try:
            from utils.dialog import ProxyDialog
            dialog = ProxyDialog()
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()
        except Exception as e:
            print(e)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())