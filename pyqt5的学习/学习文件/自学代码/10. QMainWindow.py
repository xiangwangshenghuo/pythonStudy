import sys
from PyQt5.Qt import *

class ChatWindow(QMainWindow):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QQ")
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.chatWindowWidth = 700
        self.chatWindowHeight = 500
        # 设置窗口最小尺寸为 700 500
        self.setMinimumSize(self.chatWindowWidth,self.chatWindowHeight)
        self.setStyleSheet("background-color: white;")
        # 当前用户
        self.user = user

        self.setup_ui()

    def setup_ui(self):
        # 最外层水平布局：主布局
        primaryHBL = QHBoxLayout()

        primaryHBL.setContentsMargins(0,0,0,0)
        # 设置整体布局为primaryHBL
        self.setLayout(primaryHBL)
        # 三个垂直布局
        # 1.左侧布局：添加自己头像，消息按钮，好友等，待完成
        leftVBL = QVBoxLayout()
        leftWiget = QWidget(self)
        leftWiget.setStyleSheet("background-color: black;")
        # 设置leftWiget的固定宽度和高度
        leftWiget.setFixedWidth(55)
        # 设置leftWiget的大小策略为固定大小
        leftWiget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # 添加头像框
        avatarLb = QLabel('头像框',leftWiget)
        avatarLb.setFixedSize(36,36)
        avatarLb.setStyleSheet("background-color: black;")

        leftVBL.addWidget(leftWiget)
        # leftVBL.addStretch(1)  # 添加拉伸因子使LeftWidget的高度自动撑起
        # leftVBL.addWidget(QLabel('左边'))
        # 2. 中间布局：搜索框，添加好友按钮以及群聊列表，好友列表，
        midVBL = QVBoxLayout()
        # 群聊列表
        self.groupListWidget = QListWidget(self)
        self.groupListWidget.setStyleSheet("border:none;font-size:14px;")
        # self.groupListWidget.setGeometry(10, 50, 210, 500)
        # self.groupListWidget.move(55, 60)
        # 设置groupListWidget的固定宽度和高度
        self.groupListWidget.setFixedWidth(210)
        # 设置groupListWidget的大小策略为固定大小
        self.groupListWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        for i in range(50):
            self.groupListWidget.addItem('童程童美')
            item = QListWidgetItem('小天才')
            item.setData(Qt.UserRole, 0)
            self.groupListWidget.addItem(item)
        # 把群聊列表添加到中间布局
        midVBL.addWidget(self.groupListWidget)
        # 3. 右侧布局：好友或者群聊名称，消息列表以及文本输入框
        rightVBL = QVBoxLayout()

        # 添加这三个布局
        primaryHBL.addLayout(leftVBL)
        primaryHBL.addLayout(midVBL)
        primaryHBL.addLayout(rightVBL, 1)




if __name__ == "__main__":

    app = QApplication(sys.argv)


    chatWindow = ChatWindow()

    chatWindow.show()

    sys.exit(app.exec_())

