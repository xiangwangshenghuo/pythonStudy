from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt5.QtWidgets import QMessageBox, QHBoxLayout,QTextEdit, QPushButton
from PyQt5.QtCore import Qt
import os
import json


class AlertDialog(QDialog):

    def __init__(self,*arg,**kwargs):
        super(AlertDialog, self).__init__(*arg,**kwargs)
        self.field_dict = {}
        # 初始化弹窗ui界面
        self.init_ui()

    def init_ui(self):
        """初始化对话框"""
        self.setWindowTitle("报警邮件配置")
        self.resize(300,270)

        layout = QVBoxLayout()

        form_data_list = [
            {"title":"SMTP服务器","filed":"smtp"},
            {"title":"发件箱","filed":"from"},
            {"title":"密码","filed":"pwd"},
            {"title":"收件人(多个用逗号分割)","filed":"to"},
        ]
        #读取文件中的配置
        old_alert_dict = {}
        alert_file_path = os.path.join("db", 'alert.json')
        if os.path.exists(alert_file_path):
            print(1)
            file_object = open(os.path.join("db", 'alert.json'), mode='r', encoding='utf-8')
            old_alert_dict = json.load(file_object)
            print(old_alert_dict)
            file_object.close()
        for item in form_data_list:
            lbl = QLabel()
            lbl.setText(item['title'])
            layout.addWidget(lbl)
            txt = QLineEdit()
            filed = item['filed']
            if old_alert_dict and filed in old_alert_dict:
                txt.setText(old_alert_dict[filed])
            layout.addWidget(txt)
            self.field_dict[item['filed']] = txt

        btn_save = QPushButton('保存')

        btn_save.clicked.connect(self.evet_save_click)
        layout.addWidget(btn_save,0,Qt.AlignRight)

        layout.addStretch(1)
        # 把layout渲染出来
        self.setLayout(layout)

    def evet_save_click(self):
        data_dict = {}
        for key,filed in self.field_dict.items():
            value = filed.text().strip()
            if not value:
                QMessageBox.warning(self,'错误','邮件报警项不能为空')
                return
            data_dict[key] = value
        print(data_dict)

        file_object = open(os.path.join("db",'alert.json'),mode='w',encoding='utf-8')
        json.dump(data_dict,file_object)
        file_object.close()
        # 关闭对话框
        self.close()
        pass


class ProxyDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(ProxyDialog, self).__init__(*args, **kwargs)
        self.resize(500,400)
        self.setWindowTitle('设置代理ip')
        layout = QVBoxLayout()

        # 多行输入框
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('可用换行 来设置多个代理ip，代理ip格式为：31.40.225.250:3128')
        # 默认输入文本
        path= os.path.join('db','proxy.txt')
        all_proxy = ''
        if os.path.exists(path):
            with open(os.path.join('db','proxy.txt'),mode='r',encoding='utf-8') as f:
                all_proxy = f.read()
        self.text_edit.setText(all_proxy)
        layout.addWidget(self.text_edit)

        footer_config = QHBoxLayout()
        btn_save = QPushButton('重置')
        btn_save.clicked.connect(self.event_save_click)
        footer_config.addWidget(btn_save,0,Qt.AlignRight)
        layout.addLayout(footer_config)

        self.setLayout(layout)

    def event_save_click(self):
        # 获取多行文本
        text = self.text_edit.toPlainText()

        # 写入代理
        with open(os.path.join('db','proxy.txt'),mode='w',encoding='utf-8') as f:
            f.write(text)
        print(text)

        self.close()
        pass


class LogDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('日志信息')
        self.resize(500,400)
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setText("")
        layout.addWidget(text_edit)
        # 在窗口上渲染布局
        self.setLayout(layout)

        # 读取日志展示出来



