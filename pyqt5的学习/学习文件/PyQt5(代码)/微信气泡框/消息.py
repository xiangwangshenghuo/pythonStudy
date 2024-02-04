from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys


class ChatItemWidget(QWidget):
    def __init__(self, userInfo, parent=None):
        super(ChatItemWidget, self).__init__(parent)

        # 创建水平布局，并将头像和消息添加到布局中
        layoutH = QHBoxLayout()
        self.setLayout(layoutH)

        # 创建头像
        avatar_label = QLabel()
        pixmap = QPixmap(userInfo['avatar_path'])
        avatar_label.setPixmap(pixmap.scaled(45,45))
        layoutH.addWidget(avatar_label)

        # 创建垂直布局
        layoutV = QVBoxLayout()
        # 创建昵称
        nickname_lable = QLabel(userInfo['nickname'])
        nickname_lable.setStyleSheet('padding:8px;')
        layoutV.addWidget(nickname_lable)

        layoutH2 = QHBoxLayout()
        # 创建消息框指向标志
        triangle_label = QLabel()
        triangle_label.resize(8, 10)

        pixmap = QPixmap('triangle.png')
        triangle_label.setPixmap(pixmap.scaled(8, 10))
        layoutH2.addWidget(triangle_label)
        # 创建消息文本框
        message_label = QLabel(userInfo['message'])
        message_label.setStyleSheet('background-color:#12B7F5;border-radius:15;font-size: 20px;padding:10px;')
        layoutH2.addWidget(message_label)
        layoutH2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layoutH2.setSpacing(0)
        layoutV.addLayout(layoutH2)
        layoutH.addLayout(layoutV)
        layoutH.setAlignment(Qt.AlignLeft)
        layoutH.setSpacing(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = 'wo'
    userInfo1 = {'avatar_path': "chatHead.png", 'message': "Hello!", 'nickname': '美女'}
    userInfo2 = {'avatar_path': "chatHead.png", 'message': "How are youdsfag?", 'nickname': '帅哥'}

    list_widget = QListWidget()
    list_widget.setGeometry(220, 50, 485, 340)

    # 添加聊天项
    item = QListWidgetItem(list_widget)
    # item.setText('为本')
    widget = ChatItemWidget(userInfo1)
    item.setSizeHint(widget.sizeHint())
    list_widget.setItemWidget(item, widget)

    item.setTextAlignment(Qt.AlignRight)

    item = QListWidgetItem(list_widget)
    widget = ChatItemWidget(userInfo2)
    item.setSizeHint(widget.sizeHint())
    list_widget.setItemWidget(item, widget)

    # layout = QVBoxLayout(list_widget)
    #
    # # 添加第一个聊天项
    # item = QListWidgetItem(list_widget)
    # widget = ChatItemWidget(userInfo1)
    # widget.setAlignment(Qt.AlignLeft)  # 设置控件靠左对齐
    # item.setSizeHint(widget.sizeHint())
    # list_widget.setItemWidget(item, widget)
    # layout.addWidget(widget)
    #
    # # 添加第二个聊天项
    # item = QListWidgetItem(list_widget)
    # widget = ChatItemWidget(userInfo2)
    # widget.setAlignment(Qt.AlignRight)  # 设置控件靠右对齐
    # item.setSizeHint(widget.sizeHint())
    # list_widget.setItemWidget(item, widget)
    # layout.addWidget(widget)

    list_widget.show()

    sys.exit(app.exec_())