import random
import time
from PyQt5.QtCore import QThread,pyqtSignal
import requests
from bs4 import BeautifulSoup

HOST = "https://www.amazon.com/"
HOST_ASIN_TPL = "{}{}".format(HOST,'gp/product/')
HOST_ASIN_LIST_TPL = "{}{}".format(HOST,'gp/offer-listing')


class NewTaskThread(QThread):

    # 定义信号，触发信号，更新窗体体中的数据
    # 写参数传入实参的类型
    success = pyqtSignal(int,str,str,str)
    error = pyqtSignal(int,str,str,str)
    def __init__(self,row_index,asin,*args,**kwargs):
        super(NewTaskThread, self).__init__(*args,**kwargs)
        self.row_index = row_index
        self.asin = asin

    def run(self):
        """具体线程应该做的事"""
        try:
            url = "{}{}/".format(HOST_ASIN_TPL, self.asin)
            print('圣罗爬虫')
            title = '填好了'
            url = url
            # 使用emit触发定义好的信号，并发送数据1,"xx","xx","xx"（被v3。py文件使用）
            self.success.emit(self.row_index, self.asin, title, url)
            1/0
        except Exception as e:
            print('s')
            # 使用emit触发定义好的信号，并发送数据1,"xx","xx","xx"（被v3。py文件使用）
            title = '失败'
            self.error.emit(self.row_index, self.asin, title, str(e))


class TaskThread(QThread):
    start_signal = pyqtSignal(int)
    stop_signal = pyqtSignal(int)
    counter_signal = pyqtSignal(int)
    def __init__(self,scheduler,log_file_path,row_index,asin,*args,**kwargs):
        super(TaskThread, self).__init__(*args,**kwargs)
        self.row_index= row_index
        self.asin = asin
        self.log_file_path = log_file_path
        self.scheduler = scheduler
    def run(self):
        self.start_signal.emit(self.row_index)
        # print('线程',self.row_index,self.asin)

        # 不停执行自动更新
        while True:
            if self.scheduler.terminate:
                self.stop_signal.emit(self.row_index)
                self.scheduler.thread_list.remove(self)
                return
            time.sleep(random.randint(1,3))
            self.counter_signal.emit(self.row_index)
            with open(self.log_file_path,mode='a',encoding='utf-8') as f:
                f.write('日志\n')

            # 根据型号访问连接，更新价格


