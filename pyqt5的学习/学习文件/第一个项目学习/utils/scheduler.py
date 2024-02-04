
class Scheduler():

    def __init__(self):
        self.thread_list = []
        self.window = None
        self.terminate = False # 点击停止
    def start(self,base_dir,window,fn_start,fn_counter):
        self.window = window
        self.terminate = False
        # 获取当前表格中的所有数据，每一行创建一个线程去执行监控
        for row_index in range(window.table_widget.rowCount()):
            asin = window.table_widget.item(row_index,0).text().strip()
            status_text = window.table_widget.item(row_index,6).text().strip()
            import os
            if not os.path.exists(os.path.join(base_dir, 'log')):
                os.makedirs(os.path.join(base_dir, 'log'))
            log_file_path = os.path.join(base_dir, 'log','{}.log'.format(asin))
            if status_text != '待执行':
                continue

            try:
                # 每个线程 执行 并 状态实时显示在列表中 信号 + 回调
                from utils.threads import TaskThread
                # 线程要对window上更新必须传入window
                t = TaskThread(self,log_file_path,row_index,asin,window)
                t.start_signal.connect(fn_start)
                t.counter_signal.connect(fn_counter)
                t.start()
                self.thread_list.append(t)
            except Exception as e:
                print(e)

        pass

    def stop(self):
        self.terminate = True
        # 创建一个线程，去检测thread_list中的数量
    pass


# 单例模式
SCHEDULER = Scheduler()