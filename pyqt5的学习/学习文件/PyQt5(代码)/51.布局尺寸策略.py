from PyQt5.Qt import *


class Label(QLabel):

    def sizeHint(self):
        """
        建议的尺寸大小
        """
        return QSize(150,60)
    # def minimumSizeHint(self):
    #     return QSize(200,200)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label1 = Label('好好学习1')
        label1.setStyleSheet('background-color:cyan;')
        label2 = QLabel('好好学习2')
        label2.setStyleSheet('background-color:yellow;')
        label3 = QLabel('好好学习3')
        label3.setStyleSheet('background-color:red;')
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # 设置子控件的大小策略
        # 宽和高固定不变, 按照建议的尺寸大小sizeHint返回的大小
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        # 高设置最小值,按照建议的尺寸大小sizeHint返回的高的值，如果没有设置最小大值
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum)
        # 最大尺寸
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Maximum)
        # 自由
        #
        # QSizePolicy.Preferred 可以伸展和收缩，但没有优势去获取更大的；额外空间使自己的尺寸比 sizeHint的返回值更大
        # QSizePolicy.Expanding 可以伸展和收缩，它会尽可能多地去获取额外的空间，也就是比 Preferred 更具优势
        # QSízePolicy.MinimumExpanding 可以伸展和收缩，不过sizeHint0的返回值规定了widget能缩小到的最小寸 它比 Preferred 更具优势去获取额外空间
        # QSizePalicy.Ignored  忽略sizeHint(0)的作用,可以变为0
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred)
        # label2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)
        # label3.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)
        sp = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)
        # 当隐藏时是否保留
        sp.setRetainSizeWhenHidden(True)
        label1.setSizePolicy(sp)
        label1.hide()
        label1.setFixedSize(100,100) # 优先级最高



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())