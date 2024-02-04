from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget
import sys
import time


class Worker(QObject):
    finished = pyqtSignal()
    update_list = pyqtSignal(str)

    def work(self):
        for i in range(10):
            item = f"Item {i}"
            self.update_list.emit(item)
            time.sleep(5)
        self.finished.emit()


class WorkerThread(QThread):
    update_list = pyqtSignal(str)
    finished = pyqtSignal()

    def run(self):
        worker = Worker()
        worker.update_list.connect(self.update_list)
        worker.finished.connect(self.finished)
        worker.work()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)

        self.worker_thread = WorkerThread()

        self.worker_thread.update_list.connect(self.update_list_widget)
        self.worker_thread.finished.connect(self.worker_finished)

        self.worker_thread.start()

    @pyqtSlot(str)
    def update_list_widget(self, item):
        self.list_widget.addItem(item)

    @pyqtSlot()
    def worker_finished(self):
        self.worker_thread.quit()
        self.worker_thread.wait()


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec_())
