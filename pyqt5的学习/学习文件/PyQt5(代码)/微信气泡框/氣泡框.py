import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *

# meiyong
window_height = 10
# 头像绘制位置
begin_width_spacing = 20
begin_height_spacing = 16
# 头像的宽和高
icon_width = 40
icon_height = 40

# 文本宽度和高度间距
text_width_spacing = 12
text_height_spacing = 12

# 三角形的宽度
triangle_width = 6
triangle_height = 10
triangle_height_spacing = 10

# 文本的最小宽度
text_min_width = 0
min_width = 0
text_max_width = 0
real_width = 0
text_height = 0

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, data='',type_mess = 0):
        super(MyWidget, self).__init__(parent)
        self.setObjectName('myWidget')
        self.user_chat_content = data

    # 重写paintEvent 否则不能使用样式表定义外观
    def paintEvent(self, event):
        # 此函数用于初始化气泡边框的大小，决定于字数大小
        self.init_data()
        global text_min_width, min_width, text_max_width, real_width, text_height, window_height
        # 初始化QPainter对象，一支画笔
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        # 初始化画笔的大小和字体类
        font = QtGui.QFont()
        font.setFamily("实体")
        font.setPointSize(12)
        painter.setFont(font)

        # 画头像，位置参数已初始化
        icon_rect = QRect(begin_width_spacing, begin_height_spacing, icon_width, icon_height)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QBrush(QtCore.Qt.gray))
        painter.drawPixmap(icon_rect, QtGui.QPixmap(r"chatHead.png"))

        # 画框架   初始化完后，接着就是准备画框了
        # 画框架
        bubbleRect = QRect(begin_width_spacing + icon_width, begin_height_spacing,
                           triangle_width + text_width_spacing + text_max_width + text_width_spacing,
                           text_height_spacing + text_height + text_height_spacing)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QBrush(QColor(180, 180, 180)))
        painter.drawRoundedRect(bubbleRect.x() + triangle_width, bubbleRect.y(), bubbleRect.width() - triangle_width,
                                bubbleRect.height(), 18, 18)
        linearGradient = QLinearGradient(QPointF(bubbleRect.x() + triangle_width + 1, bubbleRect.y() + 1),
                                         QPointF(bubbleRect.x() + bubbleRect.width() - 1,
                                                 bubbleRect.y() + bubbleRect.height() - 1))
        # 此处是用于画出气泡边框里面的颜色，可以渐进改变
        linearGradient.setColorAt(0, QColor(151, 220, 227))
        linearGradient.setColorAt(0.25, QColor(151, 220, 227))
        linearGradient.setColorAt(0.5, QColor(151, 220, 227))
        linearGradient.setColorAt(0.75, QColor(151, 220, 227))
        linearGradient.setColorAt(1, QColor(151, 220, 227))

        # 绘制圆角矩形框
        painter.setBrush(linearGradient)
        painter.drawRoundedRect(bubbleRect.x() + triangle_width + 1, bubbleRect.y() + 1,
                                bubbleRect.width() - triangle_width - 2, bubbleRect.height() - 2, 18, 18)
        # 绘制三角
        painter.setPen(QPen(QColor(244, 164, 96)))
        painter.drawPolygon(QPointF(bubbleRect.x(), bubbleRect.y() + triangle_height_spacing - 4),
                            QPointF(bubbleRect.x() + triangle_width + 1, bubbleRect.y() + triangle_height_spacing),
                            QPointF(bubbleRect.x() + 6 + 1, bubbleRect.y() + 10 + 10))

        # 绘制边界
        painter.setPen(QPen(QColor(180, 180, 180)))
        painter.drawLine(QPointF(bubbleRect.x(), bubbleRect.y() + 10 - 4),
                         QPointF(bubbleRect.x() + 6, bubbleRect.y() + 10))
        painter.drawLine(QPointF(bubbleRect.x(), bubbleRect.y() + 10 - 4),
                         QPointF(bubbleRect.x() + 6, bubbleRect.y() + 10 + 10))

        # 画好后呢，接着就是往气泡里添加文字了
        # 画文字
        penText = QPen()
        penText.setColor(QColor(56, 56, 56))
        painter.setPen(penText)
        option = QTextOption(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        painter.drawText(
            QRectF(bubbleRect.x() + triangle_width + text_width_spacing, bubbleRect.y() + text_height_spacing,
                   text_max_width, 48), self.user_chat_content, option)

    def init_data(self):
        font = QtGui.QFont()
        font.setFamily("实体")
        font.setPointSize(12)
        # 画好后，接着就是画出气泡框，但是气泡框的大小又决定于字体的大小。对此呢，我们先量出长和宽，太长了就要换行。
        # 在PyQt5中，`QFontMetrics`类用于测量和查询字体的度量信息，例如文本的宽度、高度、字符间距等。
        # 通过创建一个`QFontMetrics`对象，你可以使用它的方法来获取字体相关的度量信息。
        # 以下是一些`QFontMetrics`类提供的常用方法：
        # - `width(text: str) -> int`：返回给定文本在当前字体上的宽度。
        # - `height() -> int`：返回当前字体的高度。
        # - `ascent() -> int`：返回当前字体中字符的ascent（字体顶部到基线的距离）。
        # - `descent() -> int`：返回当前字体中字符的descent（基线到最低字符下沿的距离）。
        # - `leading() -> int`：返回当前字体中字符的leading（不同行之间的间距）。
        # - `lineSpacing() -> int`：返回当前字体中字符行之间的间距。
        # - `boundingRect(text: str) -> QRect`：返回给定文本在当前字体上的外接矩形。
        # 通过这些方法，你可以根据所使用的字体来获取文字的度量信息，以便在布局和绘制过程中进行准确的计算和渲染。

        metrics = QFontMetrics(font)
        global text_min_width, min_width, text_max_width, real_width, text_height, window_height
        if metrics.width("A") * 2 + begin_height_spacing * 1.5 > text_width_spacing:
            text_min_width = begin_height_spacing * 1.5 - text_width_spacing
            print(text_min_width)
        else:
            text_min_width = 0
        # 没有任何文本时的最小宽
        min_width = begin_width_spacing + icon_width + triangle_width + text_width_spacing + text_width_spacing + icon_width + begin_width_spacing
        # 判断是否超过当前框的宽
        print('chaoei', self.width(), min_width + text_min_width)

        if self.width() < min_width + text_min_width:
            self.setMinimumWidth(min_width + text_min_width)
        text_max_width = self.width() - min_width
        print('最大文本长度', text_max_width)
        real_width = metrics.width(self.user_chat_content)
        print('真实文本长度',real_width)
        if real_width < text_max_width:
            print(1)
            text_max_width = real_width
            if text_height_spacing + metrics.height() + text_height_spacing > triangle_height_spacing + triangle_height + triangle_height_spacing:
                text_height = metrics.height()
            else:
                text_height = triangle_height_spacing + triangle_height + triangle_height_spacing
        else:
            flag = QtCore.Qt.TextWordWrap
            textRect = QRect(0, 0, text_max_width, 0)
            # 自动换行
            textRect = metrics.boundingRect(textRect, flag, self.user_chat_content)
            print('自动唤醒',textRect)
            text_height = textRect.height()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_widget = QListWidget()

    # 添加聊天项
    item = QListWidgetItem(list_widget)
    widget = MyWidget("chatHead.png", "Hello!")
    item.setSizeHint(widget.sizeHint())
    list_widget.setItemWidget(item, widget)

    item = QListWidgetItem(list_widget)
    widget = MyWidget("chatHead.png", "How are youdsfag?"*100)
    item.setSizeHint(widget.sizeHint())
    list_widget.setItemWidget(item, widget)

    list_widget.show()

    sys.exit(app.exec_())